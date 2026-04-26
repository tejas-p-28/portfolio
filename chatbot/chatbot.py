import os
import json
import requests
from pathlib import Path

# Configuration for Groq API
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Load personal info from portfolio data (e.g., settings or models)
# For simplicity, we load a JSON file containing Q&A pairs.
DATA_FILE = Path(__file__).parent / "data.json"

if not DATA_FILE.exists():
    # Create a default data file with placeholder Q&A
    default_data = {
        "questions": [
            {
                "question": "What is your name?",
                "answer": "My name is [Your Name]."
            },
            {
                "question": "What is your profession?",
                "answer": "I am a web developer and designer."
            }
        ]
    }
    DATA_FILE.write_text(json.dumps(default_data, indent=2))

# Load data
with DATA_FILE.open("r", encoding="utf-8") as f:
    data = json.load(f)

# Helper to get answer from data
def get_answer(question: str) -> str:
    for qa in data.get("questions", []):
        if qa["question"].lower() in question.lower():
            return qa["answer"]
    return "I don't know the answer to that question."

# Function to call Groq API for LLM response
def chat_with_groq(messages):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {"GROQ_API_KEY}"}",
    }
    payload = {
        "model": "llama3-8b-8192",
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 512,
    }
    response = requests.post(GROQ_API_URL, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()

# Main chatbot function
def ask(question: str) -> str:
    # First try to answer from local data
    local_answer = get_answer(question)
    if local_answer != "I don't know the answer to that question.":
        return local_answer
    # If not found, ask LLM
    messages = [
        {"role": "system", "content": "You are a helpful assistant that answers questions about the user's portfolio."},
        {"role": "user", "content": question},
    ]
    result = chat_with_groq(messages)
    return result["choices"][0]["message"]["content"].strip()

if __name__ == "__main__":
    print("Chatbot ready. Type your question (or 'exit').")
    while True:
        q = input("> ")
        if q.lower() in {"exit", "quit"}:
            break
        print(ask(q))
