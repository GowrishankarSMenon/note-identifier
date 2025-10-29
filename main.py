"""
Entry point. Keeps same UX:
 - Press 'r' to start recording
 - Press 's' to stop recording
After stopping: analyze -> plot -> option to playback
"""

from audio.record_audio import record_audio
from pitch.pitch_detection import analyze_audio
from ui.screen import show_results_and_prompt

def on_recording_stopped(waveform, sr):
    """Callback passed to record_audio — called when user stops recording."""
    result = analyze_audio(waveform, sr)
    show_results_and_prompt(result)

if __name__ == "__main__":
    print("Note Identifier - press 'r' to start recording, 's' to stop.")
    record_audio(on_recording_stopped)
