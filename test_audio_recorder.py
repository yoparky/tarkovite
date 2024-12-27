from modules.audio_recorder import AudioRecorder

def test_audio_recorder():
    """
    Test the AudioRecorder class by recording a short audio clip.
    """
    # Initialize the AudioRecorder
    recorder = AudioRecorder()

    # Record a 5-second audio clip
    audio_file = recorder.record(duration=5, output_path="test_audio.wav")

    # Check if the file was created
    try:
        with open(audio_file, "rb") as f:
            print("Audio file created successfully:", audio_file)
    except FileNotFoundError:
        print("Test failed: Audio file was not created.")

if __name__ == "__main__":
    test_audio_recorder()
