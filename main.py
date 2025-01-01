import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.agents import Tool
import tarkovite_llm  # Import after complete implementation 

# Load the .env file to retrieve the OpenAI API key
load_dotenv()

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

# Initialize the OpenAI LLM with tools
llm_with_tools = OpenAILLMWithTools(model="gpt-4", temperature=0.7, retries=3, tools=tools, verbose=True)

# Main loop
if __name__ == "__main__":
    print("Tarkov Query Agent is running. Type 'exit' to quit.")
    while True:
        user_input = input("Your query: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # Generate a response from the LLM
        response = llm_with_tools.generate_response(query=user_input)
        print(response)
