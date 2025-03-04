// src/components/Recorder.js
import React, { useRef, useState } from 'react';

function Recorder({ onStop }) {
  const [recording, setRecording] = useState(false);
  const mediaRecorderRef = useRef(null);
  const audioChunks = useRef([]);

  const startRecording = async () => {
    // Request microphone access and start recording
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    mediaRecorderRef.current = new MediaRecorder(stream);
    audioChunks.current = [];

    mediaRecorderRef.current.ondataavailable = event => {
      if (event.data.size > 0) {
        audioChunks.current.push(event.data);
      }
    };

    mediaRecorderRef.current.onstop = () => {
      // Create a blob from collected audio chunks
      const audioBlob = new Blob(audioChunks.current, { type: 'audio/webm' });
      onStop(audioBlob);  // pass blob to parent component for handling
      audioChunks.current = [];
    };

    mediaRecorderRef.current.start();
    setRecording(true);
  };

  const stopRecording = () => {
    if (mediaRecorderRef.current) {
      mediaRecorderRef.current.stop();
      setRecording(false);
    }
  };

  return (
    <div className="recorder">
      {recording ? (
        <button onClick={stopRecording}>⏹ Stop Recording</button>
      ) : (
        <button onClick={startRecording}>🎙 Start Recording</button>
      )}
    </div>
  );
}

export default Recorder;
