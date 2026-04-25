from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from importlib.util import find_spec


def main() -> int:
    base = Path(__file__).resolve().parent
    if find_spec("PyInstaller") is None:
        print("PyInstaller is not installed. Run: python -m pip install pyinstaller", file=sys.stderr)
        return 1

    name = "sam-python"
    cmd = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--clean",
        str(base / "sam-python.spec"),
    ]
    print(f"Building dist/{name}{'.exe' if sys.platform == 'win32' else ''}")
    return subprocess.call(cmd, cwd=str(base))


if __name__ == "__main__":
    raise SystemExit(main())
