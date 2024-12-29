import os
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.schema import Document

def build_faiss_vectorstore():
    """
    Builds a FAISS vector store using placeholder data.
    Replace `docs` with actual data when available.
    """
    # Use OpenAI embeddings for vectorization
    embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
    
    # Placeholder documents
    docs = [
        Document(page_content="To fix your armor in Escape from Tarkov, go to Prapor or Mechanic."),
        Document(page_content="To extract safely, find an extraction point on your map."),
        Document(page_content="You can increase stamina by leveling up your Endurance skill."),
        Document(page_content="Use the flea market to buy and sell items after reaching level 15."),
    ]

    # Create the FAISS vector store
    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local("tarkov_faiss_index")
    print("FAISS Vector Store created and saved locally.")
    return vectorstore

def load_faiss_vectorstore():
    """
    Loads the FAISS vector store from disk.
    """
    embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
    vectorstore = FAISS.load_local("tarkov_faiss_index", embeddings)
    print("FAISS Vector Store loaded successfully.")
    return vectorstore

def retrieve_from_vectorstore(query, vectorstore, top_k=2):
    """
    Retrieves the top-k most relevant documents for a given query.
    """
    docs = vectorstore.similarity_search(query, k=top_k)
    return docs
