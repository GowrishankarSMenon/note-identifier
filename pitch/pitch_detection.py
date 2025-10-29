import numpy as np
from scipy.fft import rfft, rfftfreq

A4_FREQ = 440.0
NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def freq_to_note_name(frequency: float):
    if frequency <= 0:
        return None
    note_number = 69 + 12 * np.log2(frequency / A4_FREQ)
    note_index = int(round(note_number)) % 12
    octave = int((round(note_number) // 12) - 1)
    return f"{NOTES[note_index]}{octave}"

def analyze_audio(data, sr):
    """Returns FFT data and note info."""
    if len(data) == 0:
        print("No audio captured.")
        return {}

    N = len(data)
    yf = np.abs(rfft(data))
    xf = rfftfreq(N, 1 / sr)

    idx = np.argmax(yf)
    dominant_freq = xf[idx]
    note_name = freq_to_note_name(dominant_freq)

    print(f"\n=== Analysis Result ===")
    print(f"Detected note: {note_name} ({dominant_freq:.2f} Hz)")

    return {
        "waveform": data,
        "sr": sr,
        "xf": xf,
        "yf": yf,
        "dominant_freq": dominant_freq,
        "note_name": note_name
    }
