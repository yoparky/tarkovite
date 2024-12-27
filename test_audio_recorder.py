from modules.audio_recorder import AudioRecorder
from modules.audio_transcriber import AudioTranscriber

def test_audio_pipeline():
    """
    Test the full audio pipeline:
    1. Record audio.
    2. Transcribe the recorded audio.
    """
    # Step 1: Test Audio Recording
    print("Starting audio recording test...")
    recorder = AudioRecorder()
    audio_file = recorder.record(duration=5, output_path="test_audio.wav")
    
    # Verify the file was created
    try:
        with open(audio_file, "rb") as f:
            print(f"Audio file created successfully: {audio_file}")
    except FileNotFoundError:
        print("Test failed: Audio file was not created.")
        return
    
    # Step 2: Test Audio Transcription
    print("\nStarting audio transcription test...")
    transcriber = AudioTranscriber(model_name="base")  # You can change 'base' to another Whisper model if needed
    transcript = transcriber.transcribe(audio_file)
    
    # Output the transcription result
    if transcript.strip():
        print("\nTranscription Result:")
        print(transcript)
    else:
        print("Test failed: No transcription result. Audio may have been empty or unclear.")

if __name__ == "__main__":
    test_audio_pipeline()
