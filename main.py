from audio.recorder import load_audio
from pitch.detector import detect_pitch
from pitch.note_mapper import frequency_to_note_name

def main():
    y, sr = load_audio('example.wav')
    pitch = detect_pitch(y, sr)
    note = frequency_to_note_name(pitch)
    print(f"Detected note: {note} at frequency: {pitch:.2f} Hz")

if __name__ == "__main__":
    main()