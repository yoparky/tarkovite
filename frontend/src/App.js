// src/App.js
import React, { useState } from 'react';
import Recorder from './components/Recorder';
import { transcribeAudio, askQuestion } from './services/api';

function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmitQuestion = async () => {
    if (!question.trim()) return;
    setLoading(true);
    setAnswer("");
    setError("");
    try {
      const result = await askQuestion(question.trim());
      if (result.answer) {
        setAnswer(result.answer);
      }
    } catch (err) {
      console.error(err);
      setError(err.message || "Failed to get answer");
    } finally {
      setLoading(false);
    }
  };

  const handleAudioRecorded = async (audioBlob) => {
    // When recording stops, this gets called with the audio blob
    setLoading(true);
    setAnswer("");
    setError("");
    try {
      const { text } = await transcribeAudio(audioBlob);
      setQuestion(text);
      // Optionally, auto-submit the transcribed question to get an answer:
      if (text) {
        const result = await askQuestion(text);
        if (result.answer) {
          setAnswer(result.answer);
        }
      }
    } catch (err) {
      console.error(err);
      setError(err.message || "Audio processing failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App" style={{ maxWidth: '600px', margin: '2rem auto', fontFamily: 'Arial, sans-serif' }}>
      <h1>LLM RAG Q&amp;A</h1>
      <p>Ask a question by typing or speaking. All requests require a valid API key.</p>
      
      {/* Question Input */}
      <textarea
        rows="3"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Type your question here..."
        style={{ width: '100%', padding: '0.5rem' }}
      />
      <button onClick={handleSubmitQuestion} disabled={loading || !question.trim()}>
        Submit Question
      </button>
      
      {/* Audio Recorder */}
      <Recorder onStop={handleAudioRecorded} />
      
      {/* Loading and Response */}
      {loading && <p>Loading...</p>}
      {error && <p style={{ color: 'red' }}>Error: {error}</p>}
      {answer && !loading && (
        <div style={{ marginTop: '1rem', background: '#f9f9f9', padding: '1rem', borderRadius: '5px' }}>
          <strong>Answer:</strong>
          <p>{answer}</p>
        </div>
      )}
    </div>
  );
}

export default App;
