# sam-python

## Contents
- [Русский](#русский)
- [English](#english)

## Русский

### О проекте
`sam-python` - самостоятельный Python-порт синтезатора речи SAM. Основная реализация находится в `sam/samtts_native/`, CLI и интеграционная обвязка находятся в `sam/`.

Оригинальный проект: https://github.com/discordier/sam

### Структура
- `sam/` - Python-пакет и CLI.
- `sam/samtts_native/` - порт движка SAM.
- `sam-python.spec` - spec-файл PyInstaller.

### Возможности
- Синтез английской речи в WAV.
- Ввод текста через `--text` или stdin.
- Параметры SAM: `--speed`, `--pitch`, `--mouth`, `--throat`, `--singmode`, `--phonetic`.
- Запуск из исходников или как один собранный исполняемый файл.
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

### Сборка исполняемого файла
PyInstaller собирает бинарник под текущую ОС:
- Linux: `dist/sam-python`
- Windows: `dist\sam-python.exe`

```bash
python -m pip install pyinstaller
python -m PyInstaller --clean sam-python.spec
```

### Быстрая проверка
```bash
python -m sam --text "Test" --out /tmp/sam-python-test.wav
```

## English

### About
`sam-python` is a standalone Python port of the SAM text-to-speech synthesizer. The core implementation lives in `sam/samtts_native/`; the CLI and integration layer live in `sam/`.

Original project: https://github.com/discordier/sam

### Layout
- `sam/` - Python package and CLI.
- `sam/samtts_native/` - SAM engine port.
- `sam-python.spec` - PyInstaller spec file.

### Features
- English speech synthesis to WAV.
- Text input through `--text` or stdin.
- SAM controls: `--speed`, `--pitch`, `--mouth`, `--throat`, `--singmode`, `--phonetic`.
- Runs from source or as a bundled executable.
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

### Build Executable
PyInstaller builds for the current OS:
- Linux: `dist/sam-python`
- Windows: `dist\sam-python.exe`

```bash
python -m pip install pyinstaller
python -m PyInstaller --clean sam-python.spec
```

### Smoke Test
```bash
python -m sam --text "Test" --out /tmp/sam-python-test.wav
```
