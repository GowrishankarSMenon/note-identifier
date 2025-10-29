# Audio Visualizer with Playback Line (PyOpenGL + Pygame)

A real-time audio waveform visualizer built using **PyOpenGL** and **Pygame**, featuring:
- Fullscreen playback window  
- Play button integrated into the screen  
- Animated waveform display  
- Moving playback line synced with audio progress  

---

## 🧩 Features

- Visualizes waveform data from an audio file (`.wav`)
- Smooth playback animation using OpenGL
- Horizontal line that moves along the waveform during playback
- In-screen play/pause button
- Fullscreen immersive window experience

---

## ⚙️ Requirements

Make sure you have Python 3.9+ installed.

Install dependencies:

```bash
pip install pygame PyOpenGL numpy scipy
If scipy fails to install, try:

bash
Copy code
pip install scipy==1.10.1
▶️ Usage
Place your audio file (e.g., audio.wav) in the same folder as the script.

Run the script:

bash
Copy code
python main.py
When the window opens:

Click the Play button to start playback.

A horizontal white line will move along the waveform as the audio plays.

📁 Project Structure
css
Copy code
audio-visualizer/
│
├── main.py              # Main program file
├── audio.wav            # Your input audio file
└── README.md            # This file
🧠 How It Works
The waveform is computed using the FFT (Fast Fourier Transform).

The data is rendered using OpenGL line primitives.

A timer keeps track of playback progress, and the moving line is drawn based on elapsed time.

The Play button triggers the pygame.mixer audio playback and resets the line position.

🧑‍💻 Controls
Action	Description
🖱️ Click “Play”	Start audio playback
⎋ Esc	Quit the visualizer

🖼️ Screenshot (Concept)
pgsql
Copy code
 ---------------------------------------------------------
|                                                         |
|           ▄▄▄▄▄▄       ▄▄       ▄▄                      |
|         ▄▀      ▀▄   ▄▀  ▀▄   ▄▀  ▀▄                    |
|   Line → ───────────────────────────────►                |
|                                                         |
|                   [▶ Play]                              |
 ---------------------------------------------------------
📜 License
MIT License © 2025 Kannan
Feel free to modify, use, and distribute this code for learning and creative purposes.

❤️ Acknowledgements
PyOpenGL

Pygame

NumPy

SciPy

yaml
Copy code

---