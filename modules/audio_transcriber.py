import whisper
import os


class AudioTranscriber:
    def __init__(self, model_name="base"):
        """
        Initialize the Whisper model.
        :param model_name: The size of the Whisper model to use (e.g., 'tiny', 'base', 'small', 'medium', 'large').
        """
        print("Loading Whisper model...")
        self.model = whisper.load_model(model_name)
        print(f"Whisper model '{model_name}' loaded!")

    def transcribe(self, audio_path):
        """
        Transcribe the given audio file into text.
        :param audio_path: Path to the audio file to transcribe.
        :return: Transcription text.
        """
        if not os.path.exists(audio_path):
            raise FileNotFoundError(f"Audio file not found: {audio_path}")

        print("Transcribing audio...")
        result = self.model.transcribe(audio_path)
        print("Transcription completed!")

        return result["text"]
