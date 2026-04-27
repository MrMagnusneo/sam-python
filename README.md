# sam-python

## Contents
- [Русский](#русский)
- [English](#english)

## Русский

### О проекте
`sam-python` - самостоятельный Python-порт синтезатора речи SAM. Основная реализация находится в `sam/samtts_native/`, CLI и интеграционная обвязка находятся в `sam/`.

Оригинальные репозитории:
- https://github.com/discordier/sam
- https://github.com/jacklinquan/samtts

### Структура
- `sam/` - Python-пакет, CLI и API.
- `sam/samtts_native/` - порт движка SAM.
- `sam-python.spec` - spec-файл PyInstaller.

### Возможности
- Синтез английской речи в WAV.
- Ввод текста через `--text` или stdin.
- Параметры SAM: `--speed`, `--pitch`, `--mouth`, `--throat`, `--singmode`, `--phonetic`.
- Python API через `SamPythonEngine`.
- Сборка одного исполняемого файла для текущей ОС.
- Node.js runtime не требуется.

### Запуск из исходников
Требования:
- Python 3.9+

```bash
cd /home/x13/VScodeProjects/tts/sam-python
python -m sam --text "Hello from Python" --out hello.wav
```

CLI после установки пакета:

```bash
sam-python --text "Hello from Python" --out hello.wav
```

### Примеры голосов
У SAM один базовый голос; характер звучания меняется параметрами `--speed`, `--pitch`, `--mouth` и `--throat`.

| Голос | Параметры | Пример |
| --- | --- | --- |
| SAM | По умолчанию | `python -m sam --text "Hello, world!" --out sam.wav` |

### Python API
```python
from sam import SamPythonEngine

engine = SamPythonEngine()
wav_bytes = engine.synthesize_wav("Hello, world!")
```

### Сборка исполняемого файла
PyInstaller собирает бинарник под текущую ОС:
- Linux: `dist/sam-python`
- Windows: `dist\sam-python.exe`

Команды одинаковые для Linux и Windows. На Windows можно заменить `python` на `py`, если так настроен Python Launcher.

```bash
python -m pip install pyinstaller
python -m PyInstaller --clean sam-python.spec
```

### Проверка
```bash
python -m sam --text "Test" --out /tmp/sam-python-test.wav
```

## English

### About
`sam-python` is a standalone Python port of the SAM text-to-speech synthesizer. The core implementation lives in `sam/samtts_native/`; the CLI and integration layer live in `sam/`.

Original repositories:
- https://github.com/discordier/sam
- https://github.com/jacklinquan/samtts

### Layout
- `sam/` - Python package, CLI, and API.
- `sam/samtts_native/` - SAM engine port.
- `sam-python.spec` - PyInstaller spec file.

### Features
- English speech synthesis to WAV.
- Text input through `--text` or stdin.
- SAM controls: `--speed`, `--pitch`, `--mouth`, `--throat`, `--singmode`, `--phonetic`.
- Python API through `SamPythonEngine`.
- Single-file executable builds for the current OS.
- No Node.js runtime required.

### Run From Source
Requirements:
- Python 3.9+

```bash
cd /home/x13/VScodeProjects/tts/sam-python
python -m sam --text "Hello from Python" --out hello.wav
```

Installed CLI:

```bash
sam-python --text "Hello from Python" --out hello.wav
```

### Voice Examples
SAM has one base voice; its character is adjusted with `--speed`, `--pitch`, `--mouth`, and `--throat`.

| Voice | Parameters | Example |
| --- | --- | --- |
| SAM | Default | `python -m sam --text "Hello, world!" --out sam.wav` |

### Python API
```python
from sam import SamPythonEngine

engine = SamPythonEngine()
wav_bytes = engine.synthesize_wav("Hello, world!")
```

### Build Executable
PyInstaller builds for the current OS:
- Linux: `dist/sam-python`
- Windows: `dist\sam-python.exe`

The commands are the same on Linux and Windows. On Windows, replace `python` with `py` if that is how Python Launcher is configured.

```bash
python -m pip install pyinstaller
python -m PyInstaller --clean sam-python.spec
```

### Checks
```bash
python -m sam --text "Test" --out /tmp/sam-python-test.wav
```
