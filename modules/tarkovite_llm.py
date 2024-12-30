import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

# Load the .env file to retrieve the OpenAI API key
load_dotenv()

class OpenAILLM:
    def __init__(self, model="gpt-4", temperature=0, retries=2):
        """
        Initialize the OpenAI LLM using LangChain's ChatOpenAI.
        """
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OpenAI API key not found. Set it in the .env file.")

        self.llm = ChatOpenAI(
            model=model,
            temperature=temperature,
            max_tokens=None,
            timeout=None,
            max_retries=retries,
            openai_api_key=api_key,  # Use the retrieved API key
        )

    def generate_response(self, context, query):
        """
        Generate a response from the LLM using provided context and query.

        Args:
            context (str): Relevant context or background information.
            query (str): The user's query.

        Returns:
            str: Response from the LLM.
        """
        # Construct the augmented query with context
        augmented_query = f"Context:\n{context}\n\nQuestion: {query}"

        # Define the message structure for the LLM
        messages = [
            SystemMessage(content="You are a helpful assistant for Escape from Tarkov players."),
            HumanMessage(content=augmented_query),
        ]

        # Use the LLM to generate a response
        response = self.llm.invoke(messages)
        return response
