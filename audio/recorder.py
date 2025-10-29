import librosa

def load_audio(file_path, sr=44100):
    
    """
    Load an audio file.

    Parameters:
    file_path (str): Path to the audio file.
    sr (int): Sample rate for loading the audio.

    Returns:
    y (np.ndarray): Audio time series.
    sr (int): Sample rate of y.
    """
    y, sr = librosa.load(file_path, sr=sr)
    return y, sr