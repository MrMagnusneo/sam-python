import argparse
import sys
from pathlib import Path

from .engine import SamPythonEngine


def main() -> int:
    parser = argparse.ArgumentParser(description="Native Python SAM TTS")
    parser.add_argument("--text", help="Input text. If not set, text is read from stdin.")
    parser.add_argument("--out", default="sam.wav", help="Output WAV path")
    parser.add_argument("--speed", type=int, default=72)
    parser.add_argument("--pitch", type=int, default=64)
    parser.add_argument("--mouth", type=int, default=128)
    parser.add_argument("--throat", type=int, default=128)
    parser.add_argument("--singmode", action="store_true")
    parser.add_argument("--phonetic", action="store_true")
    args = parser.parse_args()

    text = args.text if args.text is not None else sys.stdin.read().strip()
    if not text:
        parser.error("No input text provided")

    engine = SamPythonEngine(
        speed=args.speed,
        pitch=args.pitch,
        mouth=args.mouth,
        throat=args.throat,
        singmode=args.singmode,
        phonetic=args.phonetic,
    )
    wav = engine.synthesize_wav(text)
    out_path = Path(args.out)
    out_path.write_bytes(wav)
    print(f"WAV saved to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
