import openai
from config import Config

# Set your OpenAI API key
openai.api_key = Config.OPENAI_API_KEY

def generate_answer(question: str, context_docs: list) -> str:
    """
    Generate an answer to the question using the context from retrieved docs.
    Uses OpenAI's ChatCompletion (GPT model) for response generation.
    """
    # Prepare context text from documents
    context_texts = [doc.get('content', '') for doc in context_docs]
    context_combined = "\n\n".join(context_texts[:3])  # use top 3 docs
    
    # Formulate the prompt with context and question
    prompt = (
        "You are a knowledgeable guide for the game Escape from Tarkov. Answer questions using the provided context. "
        "If the context is insufficient, use your game knowledge to provide a helpful answer.\n\n"
        "Example 1:\n"
        "Context: 'The best weapons in Tarkov are customizable.'\n"
        "Question: 'What is the best weapon in Tarkov?'\n"
        "Answer: 'The best weapon in Tarkov depends on your playstyle, but customizable weapons like the M4A1 and AK-74 are popular choices.'\n\n"
        "Now, answer the following question using the provided context:\n"
        "Context:\n"
        f"{context_combined}\n\n"
        "Question:\n"
        f"{question}\n\n"
        "Answer in a detailed yet concise manner:"
    )

    try:
        # Correct method for OpenAI API v1.0.0 and above
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7
        )
        # Extract the answer from the response
        answer = response.choices[0].message.content.strip()
        return answer
    except Exception as e:
        print(f"OpenAI API error: {e}")
        raise Exception("OpenAPI error")
