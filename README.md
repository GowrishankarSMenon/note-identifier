# 🎵 Note Identifier

A simple and extensible project to identify musical notes from audio.

## 🧱 Stage 1 — Basic Setup

- Loads an audio file
- Detects dominant pitch frequency
- Converts frequency → musical note (e.g., A4, C#5)
- Modular structure for future scalability (real-time, ML, instrument recognition)

### Directory Structure

```
note_identifier/
├── audio/
│   └── recorder.py
├── pitch/
│   ├── detector.py
│   └── note_mapper.py
├── main.py
├── README.md
└── .gitignore
```

### Setup

```bash
pip install librosa numpy sounddevice scipy
```

**Commit this:**

```bash
git add .
git commit -m "Initialize project skeleton with modular folders and base README"
```