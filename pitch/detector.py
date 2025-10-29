import librosa
import numpy as np

def detect_pitch(y, sr):
    '''
    Detect the dominant pitch frequency in an audio signal.

    Parameters:
    y (np.ndarray): Audio time series.
    sr (int): Sample rate of y.

    Returns:
    f (float): Dominant pitch frequency.
    '''
    pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
    index = magnitudes.argmax()
    pitch = pitches.flatten()[index]
    return pitch