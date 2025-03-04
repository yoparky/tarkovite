import faiss
import numpy as np
import json
import openai
import os
from config import Config

# Global variables for the FAISS index and stored documents
index = None
documents = []

# Function to generate embeddings using the OpenAI API
def embed_query(text: str):
    response = openai.Embedding.create(
        input=[text],
        model="text-embedding-ada-002"
    )
    embedding = response['data'][0]['embedding']
    return np.array(embedding, dtype=np.float32)

# Function to create or load the FAISS index
def initialize_faiss_index():
    global index, documents

    if os.path.exists(Config.FAISS_INDEX_PATH):
        print("Loading existing FAISS index...")
        index = faiss.read_index(Config.FAISS_INDEX_PATH)
        with open(Config.DOCUMENTS_PATH, 'r') as f:
            documents = json.load(f)
    else:
        print("FAISS index not found. Creating a new index...")
        with open(Config.DOCUMENTS_PATH, 'r') as f:
            documents = json.load(f)

        if not documents:
            print("No documents found for indexing.")
            return

        # Generate embeddings for all documents
        embeddings = np.array([embed_query(doc['content']) for doc in documents], dtype=np.float32)

        # Initialize FAISS index
        dimension = len(embeddings[0])
        index = faiss.IndexFlatL2(dimension)
        index.add(embeddings)

        # Save the index to disk
        faiss.write_index(index, Config.FAISS_INDEX_PATH)
        print("FAISS index created and saved.")

# Function to search the FAISS index
def search_vectors(query: str, k: int = 5):
    if index is None:
        print("FAISS index is not initialized.")
        return []
    
    query_vector = embed_query(query).reshape(1, -1)
    distances, indices = index.search(query_vector, k)
    
    return [documents[i] for i in indices[0] if i < len(documents)]

# Initialize the FAISS index when the module is imported
initialize_faiss_index()
