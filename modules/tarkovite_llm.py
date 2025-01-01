import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

# Load the .env file to retrieve the OpenAI API key
load_dotenv()

from langchain.llms import OpenAI
from langchain.agents import initialize_agent, Tool

# Initialize LLM
llm = OpenAI(model="gpt-3.5-turbo", openai_api_key=os.getenv("OPENAI_API_KEY"))

# Define tools
tools = [
    Tool(
        name="Get All Quests",
        func=get_all_quests_tool,
        description="Retrieve all quests from the Tarkov API, including objectives and details."
    ),
    Tool(
        name="Get Item Data",
        func=get_item_data_tool,
        description="Retrieve detailed information about a specific item by providing its name."
    ),
    Tool(
        name="Get All Item Data",
        func=get_all_item_data_tool,
        description="Retrieve information about the predefined item 'colt m4a1'."
    ),
    Tool(
        name="Get Server Status",
        func=get_server_status_tool,
        description="Retrieve the current server status and related messages from the Tarkov API."
    )
]

# Initialize the agent
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from langchain.agents import initialize_agent, Tool

class OpenAILLMWithTools:
    def __init__(self, model="gpt-4", temperature=0, retries=2, tools=None, verbose=True):
        """
        Initialize the OpenAI LLM using LangChain's ChatOpenAI and set up tools.

        Args:
            model (str): The OpenAI model to use (default: "gpt-4").
            temperature (float): Sampling temperature for creativity (default: 0 for deterministic output).
            retries (int): Maximum number of retries for API calls (default: 2).
            tools (list): List of LangChain Tool objects (default: None).
            verbose (bool): Whether to log agent activity (default: True).
        """
        # Load the API key from environment variables
        load_dotenv()  # Ensure the .env file is loaded
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OpenAI API key not found. Set it in the .env file.")

        # Initialize the ChatOpenAI object
        self.llm = ChatOpenAI(
            model=model,
            temperature=temperature,
            max_tokens=None,
            timeout=None,
            max_retries=retries,
            openai_api_key=api_key,
        )

        # Initialize tools
        self.tools = tools or []
        self.verbose = verbose

        # Initialize the agent if tools are provided
        if self.tools:
            self.agent = initialize_agent(
                tools=self.tools,
                llm=self.llm,
                agent="zero-shot-react-description",
                verbose=self.verbose,
            )
        else:
            self.agent = None

    def generate_response(self, query, context=None):
        """
        Generate a response from the LLM using the provided query and optional context.

        Args:
            query (str): The user's query.
            context (str, optional): Relevant context or background information (default: None).

        Returns:
            str: Response generated by the LLM.
        """
        # Construct the prompt with context if provided
        if context:
            augmented_query = f"Context:\n{context}\n\nQuestion: {query}"
        else:
            augmented_query = query

        # Define the message structure for the LLM
        messages = [
            SystemMessage(content="You are a helpful assistant for Escape from Tarkov players."),
            HumanMessage(content=augmented_query),
        ]

        # Generate the response using the LLM
        try:
            if self.agent:  # Use the agent if tools are defined
                return self.agent.run(query)
            else:  # Fall back to basic LLM response
                response = self.llm.invoke(messages)
                return response.content  # Extract the response text
        except Exception as e:
            return f"An error occurred while generating a response: {str(e)}"
