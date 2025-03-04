import openai
from config import Config
from typing import Union
import io

# Configure OpenAI API key for Whisper
openai.api_key = Config.OPENAI_API_KEY

def transcribe_audio(audio_bytes: Union[bytes, io.BytesIO]) -> str:
    """
    Transcribe audio bytes to text using OpenAI Whisper API.
    Expects audio in a compatible format (e.g., WAV or WEBM bytes).
    """
    try:
        # Create an in-memory file from the audio bytes
        audio_file = io.BytesIO(audio_bytes)
        audio_file.name = "audio.wav"  # Give the file a name, required by OpenAI API

        # Call the OpenAI Whisper transcription API
        response = openai.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
        
        # Directly access the text attribute of the response object
        return response.text
    except Exception as e:
        print(f"Whisper API error: {e}")
        raise Exception("Whisper API error")
