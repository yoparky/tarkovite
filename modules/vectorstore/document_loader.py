from langchain.schema import Document

def load_documents(file_path):
    """
    Load text data from a file and convert it to a list of Document objects.
    """
    with open(file_path, "r") as f:
        lines = f.readlines()
    docs = [Document(page_content=line.strip()) for line in lines if line.strip()]
    print(f"Loaded {len(docs)} documents from {file_path}")
    return docs
