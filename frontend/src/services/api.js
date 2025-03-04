// src/services/api.js
const API_BASE = process.env.REACT_APP_API_BASE_URL || "";  
const API_KEY = process.env.REACT_APP_API_KEY;              // API key for auth (set in .env file for frontend)

export async function transcribeAudio(audioBlob) {
  // Send the audio blob to the /api/transcribe endpoint
  const formData = new FormData();
  formData.append('audio', audioBlob, 'speech.webm');

  const response = await fetch(`${API_BASE}/api/transcribe`, {
    method: 'POST',
    headers: {
      'X-API-KEY': API_KEY  // include API key for auth

    },
    body: formData
  });
  if (!response.ok) {
    const errData = await response.json().catch(() => ({}));
    throw new Error(errData.error || 'Transcription request failed');
  }
  return response.json();  // { text: "transcribed text" }
}

export async function askQuestion(questionText) {
  const response = await fetch('http://localhost:5000/api/ask', {
      method: 'POST',
      mode: 'cors',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({ question: questionText })
  });

  if (!response.ok) {
      const errData = await response.json().catch(() => ({}));
      throw new Error(errData.error || 'Question request failed');
  }

  return response.json();
}
