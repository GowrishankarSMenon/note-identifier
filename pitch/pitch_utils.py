"""
Utility: map frequency (Hz) -> musical note name (e.g., A4, C#3).
Uses A4 = 440 Hz reference and MIDI note formula.
"""

import numpy as np

A4_FREQ = 440.0
NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F',
              'F#', 'G', 'G#', 'A', 'A#', 'B']

def freq_to_note_name(frequency_hz: float):
    if frequency_hz is None or frequency_hz <= 0:
        return None
    # MIDI note number
    note_num = 69 + 12 * np.log2(frequency_hz / A4_FREQ)
    note_num_rounded = int(round(note_num))
    note_index = note_num_rounded % 12
    octave = (note_num_rounded // 12) - 1
    name = NOTE_NAMES[note_index]
    return f"{name}{octave}"
