# sam-python

## Содержание / Contents
- [Русский](#русский)
- [English](#english)

## Русский

### О проекте
`sam-python` - нативный Python-порт синтезатора речи SAM. Основная реализация находится в `sam_port/samtts_native/`, CLI и интеграционный код находятся в `sam_port/`.

Оригинальный репозиторий SAM: https://github.com/discordier/sam

### Функционал
- Синтез английской речи в WAV.
- Ввод текста через `--text` или stdin.
- Настройка параметров SAM: `--speed`, `--pitch`, `--mouth`, `--throat`, `--singmode`, `--phonetic`.
- Запуск как Python-модуль или как собранный один исполняемый файл.
- Не требует Node.js runtime.

### Запуск из исходников
Требования:
- Python 3.9+

```bash
cd /home/x13/VScodeProjects/tts/sam-python
python -m sam_port --text "Hello from Python" --out hello.wav
```

### Сборка одного исполняемого файла
PyInstaller собирает исполняемый файл под ту ОС, на которой запущена сборка:
- Linux: `dist/sam-python`
- Windows: `dist\sam-python.exe`

Установите PyInstaller:
```bash
python -m pip install pyinstaller
```

Соберите проект:
```bash
python build_executable.py
```

То же самое можно сделать через spec-файл:
```bash
python -m PyInstaller --clean sam-python.spec
```

## English

### About
`sam-python` is a native Python port of the SAM text-to-speech synthesizer. The synthesizer implementation lives in `sam_port/samtts_native/`; the CLI and integration code live in `sam_port/`.

Original SAM repository: https://github.com/discordier/sam

### Features
- English speech synthesis to WAV.
- Text input via `--text` or stdin.
- SAM parameter controls: `--speed`, `--pitch`, `--mouth`, `--throat`, `--singmode`, `--phonetic`.
- Runs as a Python module or as a bundled single-file executable.
- Does not require the Node.js runtime.

### Run From Source
Requirements:
- Python 3.9+

```bash
cd /home/x13/VScodeProjects/tts/sam-python
python -m sam_port --text "Hello from Python" --out hello.wav
```

### Single-File Build
PyInstaller builds an executable for the OS where the build is run:
- Linux: `dist/sam-python`
- Windows: `dist\sam-python.exe`

Install PyInstaller:
```bash
python -m pip install pyinstaller
```

Build the project:
```bash
python build_executable.py
```

You can also build from the checked-in spec file:
```bash
python -m PyInstaller --clean sam-python.spec
```
