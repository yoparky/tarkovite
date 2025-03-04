{# Tarkovite LLM App

The **Tarkovite LLM App** is a community tool that uses a **Retrieval-Augmented Generation (RAG)** model with OpenAI's GPT-3.5-turbo and FAISS for vector search. The app allows users to ask questions about *Escape from Tarkov* via a microphone input or text and provides accurate and helpful answers using a curated knowledge base.

---

## Features:
- **Microphone Input:** Transcribe audio questions using OpenAI's Whisper model.
- **Text Input:** Supports direct question input via a simple UI.
- **LLM-Based Answering:** Uses GPT-3.5-turbo with context retrieval through FAISS.
- **Vector Search:** Quickly finds relevant information from a pre-built vector database.
- **Rate Limiting:** Prevents excessive API usage.

---

## Setup Instructions:

### 1. Clone the Repository:
```sh
git clone https://github.com/yourusername/tarkov_helper.git
cd tarkov_helper
```

### 2. Backend Setup:
```sh
cd backend
python -m venv venv           # Create a virtual environment
source venv/bin/activate       # Activate (use .\venv\Scripts\activate on Windows)
pip install -r requirements.txt # Install dependencies
python app.py                  # Start the backend server
```

### 3. Frontend Setup:
```sh
cd ../frontend
npm install                    # Install frontend dependencies
npm start                      # Start the React app
```

### 4. Environment Variables:
Create a `.env` file in both `backend` and `frontend` directories:

**Backend `.env`:**
```sh
OPENAI_API_KEY=your_openai_api_key
FAISS_INDEX_PATH=data/faiss.index
DOCUMENTS_PATH=data/documents.json
RATE_LIMIT=100 per minute
LOG_LEVEL=INFO
```

**Frontend `.env`:**
```sh
REACT_APP_API_BASE_URL=http://localhost:5000
```

---

## How to Use:
1. Open the frontend in a browser (`http://localhost:3000`).
2. Click the **microphone button** to ask a question or type directly.
3. Receive a quick and accurate response based on *Escape from Tarkov* knowledge.

---
