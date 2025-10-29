import numpy as np

A4_FREQ = 440.0
NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def frequency_to_note_name(frequency):
    if frequency <= 0:
        return None
    note_number = 12 * np.log2(frequency / A4_FREQ) + 69
    note_index = int(round(note_number)) % 12
    octave = int(round(note_number/12) - 1)
    return f"{NOTE_NAMES[note_index]}{octave}"