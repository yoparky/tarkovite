import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Load the .env file's API Key
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("OpenAI API key not found. Set it in .env file.")

model = "gpt-4o-mini"

llm = ChatOpenAI(
    model=model,
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2
)

messages = [
    (
        "system",
        "You are a helpful assistant that gives advice and answers questions for players playing the game Escape from Tarkov.",
    ),
    (
        "human", "I'm testing out the api. Do you get my message?!"
    ),
]

answer = llm.invoke(messages)
print(answer)