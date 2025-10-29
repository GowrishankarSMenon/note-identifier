import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import numpy as np
import sounddevice as sd
import threading
import time

def show_results_and_prompt(result):
    """Displays waveform, FFT, detected note, and playback button."""
    waveform = result["waveform"]
    sr = result["sr"]
    xf = result["xf"]
    yf = result["yf"]
    note_name = result["note_name"]
    dominant_freq = result["dominant_freq"]

    duration = len(waveform) / sr
    t = np.linspace(0, duration, len(waveform))

    # Windowed layout
    fig, (ax_wave, ax_fft) = plt.subplots(2, 1, figsize=(12, 8))
    plt.subplots_adjust(bottom=0.25, hspace=0.35)

    # === 1. Waveform ===
    ax_wave.plot(t, waveform, color='royalblue')
    ax_wave.set_title("🎵 Recorded Audio Waveform", fontsize=16, weight='bold')
    ax_wave.set_xlabel("Time (s)")
    ax_wave.set_ylabel("Amplitude")
    ax_wave.grid(alpha=0.3)

    # vertical line (cursor)
    cursor_line, = ax_wave.plot([0, 0], [min(waveform), max(waveform)], color='orange', linewidth=2)

    # === 2. Frequency domain ===
    ax_fft.plot(xf, yf, color='darkgreen')
    ax_fft.set_title("Frequency Spectrum (Fourier Transform)", fontsize=16, weight='bold')
    ax_fft.set_xlabel("Frequency (Hz)")
    ax_fft.set_ylabel("Magnitude")
    ax_fft.grid(alpha=0.3)
    ax_fft.axvline(x=dominant_freq, color='crimson', linestyle='--', linewidth=1.5)
    ax_fft.text(dominant_freq, max(yf) * 0.9, f"{dominant_freq:.2f} Hz", color='crimson')

    # === Note info box ===
    fig.text(0.8, 0.82, f"🎶 Detected Note:\n{note_name}\n({dominant_freq:.2f} Hz)",
             fontsize=14, color='crimson',
             bbox=dict(facecolor="white", alpha=0.8, edgecolor="black"))

    # === Play button ===
    ax_play = plt.axes([0.45, 0.08, 0.1, 0.075])
    btn_play = Button(ax_play, '▶ Play', color='lightgreen', hovercolor='lime')

    is_playing = False

    def on_play(event):
        nonlocal is_playing
        if is_playing:
            return
        is_playing = True

        threading.Thread(target=lambda: sd.play(np.array(waveform), samplerate=sr)).start()

        start_time = time.time()
        while time.time() - start_time < duration:
            x = time.time() - start_time
            cursor_line.set_xdata([x, x])
            plt.pause(0.01)
        cursor_line.set_xdata([0, 0])
        plt.draw()

        is_playing = False

    btn_play.on_clicked(on_play)

    plt.show()
