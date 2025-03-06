from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.schema import Document
from config import Config
from vector_search import get_retriever

# Initialize the OpenAI LLM with LangChain
llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=Config.OPENAI_API_KEY)

# Define a prompt template for generating answers
prompt_template = PromptTemplate(
    template=(
        "You are an expert in Escape from Tarkov. Use the provided context to answer the question. "
        "If the context is insufficient, use your game knowledge to provide a helpful answer."
        "\n\nContext: {context}\nQuestion: {question}\nAnswer:"
    ),
    input_variables=["context", "question"]
)

# Set up the RAG chain with a retriever from FAISS
retriever = get_retriever()
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)

# Function to generate answers using the RAG approach
def generate_answer(question: str) -> str:
    try:
        result = qa_chain({"query": question})
        answer = result['result']
        return answer
    except Exception as e:
        print(f"OpenAI API error: {e}")
        raise Exception("OpenAI error")
