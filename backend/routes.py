from flask import Blueprint, request, jsonify
from config import Config
from auth import require_api_key
from limiter import limiter
import speech_to_text
import vector_search
import llm

api_bp = Blueprint('api', __name__)

@api_bp.route('/ask', methods=['POST'])
#@require_api_key
@limiter.limit(Config.RATE_LIMIT)  # limit requests per client (IP)
def ask_question():
    """Handle text questions: retrieve context and get LLM answer."""
    data = request.get_json(force=True)
    question = data.get('question', '')
    if not question:
        return jsonify({"error": "No question provided"}), 400
    # Retrieve relevant documents via vector search
    docs = vector_search.search_vectors(question, k=5)
    # Generate answer using LLM
    answer = llm.generate_answer(question, docs)
    return jsonify({"answer": answer})

@api_bp.route('/transcribe', methods=['POST'])
#@require_api_key
@limiter.limit(Config.RATE_LIMIT)
def transcribe_audio_route():
    """Handle audio input: transcribe to text using Whisper."""
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file uploaded"}), 400
    audio_file = request.files['audio']
    audio_bytes = audio_file.read()
    try:
        text = speech_to_text.transcribe_audio(audio_bytes)
        return jsonify({"text": text})
    except Exception as e:
        return jsonify({"error": "Transcription failed", "details": str(e)}), 500
