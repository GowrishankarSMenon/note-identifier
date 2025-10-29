# 🎵 Note Identifier

A real-time musical note detection system that records audio, analyzes pitch using FFT, and identifies musical notes.

---

## 🧩 Features

- **Real-time audio recording** with keyboard controls ('r' to record, 's' to stop)
- **Pitch detection** using Fast Fourier Transform (FFT)
- **Musical note identification** (e.g., A4, C#5) from frequency analysis
- **Visual feedback** with waveform and frequency spectrum plots
- **Audio playback** with animated cursor showing playback position
- **Modular architecture** for easy extensibility

---

## ⚙️ Requirements

Make sure you have Python 3.9+ installed.

Install dependencies:

```bash
pip install numpy scipy sounddevice matplotlib keyboard
```

---

## ▶️ Usage

Run the main script:

```bash
python main.py
```

**Controls:**

1. Press **'r'** to start recording audio
2. Speak, sing, or play an instrument near your microphone
3. Press **'s'** to stop recording

**After recording stops:**

- The program will automatically analyze the audio
- A window will display:
  - **Waveform plot** (time domain)
  - **Frequency spectrum** (FFT analysis)
  - **Detected note** with frequency in Hz
  - **Play button** to replay the recording with animated cursor

---

## 📁 Project Structure

```
NOTE_IDENTIFIER/
│
├── audio/
│   ├── playback.py
│   └── record_audio.py
│
├── pitch/
│   ├── pitch_detection.py
│   └── pitch_utils.py
│
├── ui/
│   └── screen.py
│
├── .gitignore
├── main.py
└── README.md
```

---

## 🧠 How It Works

- The waveform is computed using the FFT (Fast Fourier Transform).
- The data is rendered using OpenGL line primitives.
- A timer keeps track of playback progress, and the moving line is drawn based on elapsed time.
- The Play button triggers the pygame.mixer audio playback and resets the line position.

---

## 🧑‍💻 Controls

| Action | Description |
|--------|-------------|
| 🖱️ Click "Play" | Start audio playback |
| ⎋ Esc | Quit the visualizer |

---

## 🖼️ Screenshot (Concept)

```
 ---------------------------------------------------------
|                                                         |
|           ▄▄▄▄▄▄       ▄▄       ▄▄                      |
|         ▄▀      ▀▄   ▄▀  ▀▄   ▄▀  ▀▄                    |
|   Line → ───────────────────────────────►               |
|                                                         |
|                   [▶ Play]                             |
 ---------------------------------------------------------
```

---

## 📜 License

☕ **Coffee License**

If this code helped you, consider buying me a coffee;) ☕

Feel free to modify, use, and distribute this code for learning and creative purposes.

---

## ❤️ Acknowledgements

- PyOpenGL
- Pygame
- NumPy
- SciPy