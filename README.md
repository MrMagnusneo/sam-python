# sam_python

Python version wrapper for SAM TTS.

## What is saved
- Native Python port is in `sam_port/samtts_native/` (no Node.js runtime required).
- Python CLI and integration code is in `sam_port/`.

## Quick start
```bash
cd /home/x13/VScodeProjects/tts/sam_python
python -m sam_port --text "Hello from Python" --out hello.wav
```

Requirements:
- Python 3.9+
