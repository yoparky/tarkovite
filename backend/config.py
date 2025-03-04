import os

class Config:
    # API Keys and endpoints
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
    OPENAI_API_BASE = os.environ.get('OPENAI_API_BASE', 'https://api.openai.com')
    ALLOWED_API_KEYS = os.environ.get('ALLOWED_API_KEYS', '').split(',')

    # Rate limiting (100 requests per minute by default, adjustable via env)
    RATE_LIMIT = os.environ.get('RATE_LIMIT', '100 per minute')

    # Paths or settings for vector database and models
    FAISS_INDEX_PATH = os.environ.get('FAISS_INDEX_PATH', 'data/faiss.index')
    DOCUMENTS_PATH = os.environ.get('DOCUMENTS_PATH', 'data/documents.json')

    # Logging settings
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')