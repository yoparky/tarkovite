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

    def add_single_document(self, text):
        """
        Add a single document to the FAISS vector store.
        """
        document = Document(page_content=text)
        try:
            vectorstore = self.load_vectorstore()
        except ValueError:
            # If vector store does not exist, create a new one
            print("No existing vector store found. Creating a new one...")
            self.build_vectorstore([document])
            return
        # Add the document to the existing vector store
        vectorstore.add_documents([document])
        vectorstore.save_local(self.index_path)
        print("Single document added to the FAISS vector store.")

    def add_multiple_documents(self, texts):
        """
        Add a list of documents to the FAISS vector store.
        Each text in the list will be treated as a separate chunk.
        """
        documents = [Document(page_content=text) for text in texts]
        try:
            vectorstore = self.load_vectorstore()
        except ValueError:
            # If vector store does not exist, create a new one
            print("No existing vector store found. Creating a new one...")
            self.build_vectorstore(documents)
            return
        # Add the documents to the existing vector store
        vectorstore.add_documents(documents)
        vectorstore.save_local(self.index_path)
        print(f"{len(texts)} documents added to the FAISS vector store.")
