import os
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.schema import Document

class FAISSVectorStore:
    def __init__(self, index_path="tarkov_faiss_index"):
        self.index_path = index_path
        self.embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))

    def build_vectorstore(self, docs):
        """
        Build a FAISS vector store from the provided documents.
        """
        vectorstore = FAISS.from_documents(docs, self.embeddings)
        vectorstore.save_local(self.index_path)
        print(f"FAISS Vector Store created at {self.index_path}")
        return vectorstore

    def load_vectorstore(self):
        """
        Load an existing FAISS vector store from disk.
        """
        if not os.path.exists(self.index_path):
            raise ValueError(f"Vector store not found at {self.index_path}.")
        vectorstore = FAISS.load_local(self.index_path, self.embeddings)
        print(f"FAISS Vector Store loaded from {self.index_path}")
        return vectorstore

    def search(self, query, k=2):
        """
        Search the vector store for the top-k most relevant documents.
        """
        vectorstore = self.load_vectorstore()
        return vectorstore.similarity_search(query, k=k)
