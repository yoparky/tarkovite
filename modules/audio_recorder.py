import sounddevice as sd
import wave
import numpy as np
import os


class AudioRecorder:
    def __init__(self, sample_rate=16000, channels=1, dtype="int16"):
        """
        Initialize the audio recorder with default parameters.
        :param sample_rate: Sampling rate for the audio (default: 16kHz).
        :param channels: Number of audio channels (default: Mono - 1 channel).
        :param dtype: Data type for the audio (default: int16).
        """
        self.sample_rate = sample_rate
        self.channels = channels
        self.dtype = dtype

    def record(self, duration=5, output_path="user_audio.wav"):
        """
        Record audio and save it as a WAV file.
        :param duration: Duration of the recording in seconds.
        :param output_path: Path to save the recorded audio file.
        :return: Path to the recorded audio file.
        """
        print("Recording... Speak now!")
        audio_data = sd.rec(
            int(duration * self.sample_rate),
            samplerate=self.sample_rate,
            channels=self.channels,
            dtype=self.dtype,
        )
        sd.wait()  # Wait for the recording to finish
        print("Recording finished!")

        # Save audio data to a WAV file
        with wave.open(output_path, "wb") as wf:
            wf.setnchannels(self.channels)
            wf.setsampwidth(np.dtype(self.dtype).itemsize)
            wf.setframerate(self.sample_rate)
            wf.writeframes(audio_data.tobytes())

        print(f"Audio saved to {output_path}")
        return output_path