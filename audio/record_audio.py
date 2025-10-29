import sounddevice as sd
import numpy as np
import keyboard

SAMPLE_RATE = 44100

def record_audio(on_stop_callback):
    """Records when 'r' pressed and stops when 's' pressed."""
    print("Press 'r' to start recording and 's' to stop recording.")
    audio_data = []
    is_recording = False

    def callback(indata, frames, time, status):
        nonlocal audio_data
        if is_recording:
            audio_data.extend(indata[:, 0])

    with sd.InputStream(callback=callback, channels=1, samplerate=SAMPLE_RATE):
        while True:
            if keyboard.is_pressed('r') and not is_recording:
                print("Recording started... Press 's' to stop.")
                audio_data = []
                is_recording = True

            if keyboard.is_pressed('s') and is_recording:
                is_recording = False
                print("Recording stopped. Duration:", f"{len(audio_data)/SAMPLE_RATE:.2f} s")
                waveform = np.array(audio_data)
                on_stop_callback(waveform, SAMPLE_RATE)
                break
