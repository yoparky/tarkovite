from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
import os
import json
from config import Config

# Load documents from the JSON file
documents = []
if os.path.exists(Config.DOCUMENTS_PATH):
    with open(Config.DOCUMENTS_PATH, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)
        documents = [Document(page_content=doc['content'], metadata=doc.get('metadata', {})) for doc in raw_data]

# Initialize the embedding model
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002", openai_api_key=Config.OPENAI_API_KEY)

# Initialize FAISS vector store
vector_store = None
if os.path.exists(Config.FAISS_INDEX_PATH):
    print("Loading existing FAISS index...")
    vector_store = FAISS.load_local(Config.FAISS_INDEX_PATH, embeddings)
else:
    print("FAISS index not found. Creating a new index...")
    vector_store = FAISS.from_documents(documents, embeddings)
    vector_store.save_local(Config.FAISS_INDEX_PATH)

# get the retriever from the vector store
def get_retriever():
    return vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 5})
