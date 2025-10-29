"""
Plays back a numpy waveform using sounddevice.
"""

import sounddevice as sd
import numpy as np

def play_audio(waveform, sample_rate):
    """Plays the mono waveform (1D numpy) at sample_rate. Non-blocking until sd.wait()."""
    if waveform is None or len(waveform) == 0:
        print("Nothing to play back.")
        return
    # ensure float32 in [-1, 1]
    x = np.asarray(waveform, dtype=np.float32)
    # normalize to avoid clipping if needed
    maxv = np.max(np.abs(x))
    if maxv > 1.0:
        x = x / maxv
    try:
        sd.play(x, samplerate=sample_rate)
        sd.wait()
    except Exception as e:
        print(f"Playback error: {e}")
