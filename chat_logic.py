from dotenv import load_dotenv
import os
from google import genai

load_dotenv() 

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def embed_text(text):
    result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )
    return result.embeddings  

MODEL = "gemini-2.5-flash"
MAX_CONTEXT_MESSAGES = 10
TEMPERATURE = 0.8

def build_prompt(system_prompt, history, user_input):
    
    # system instruction + recent messages
    parts = [f"SYSTEM: {system_prompt}\n"]
    for role, text in history[-MAX_CONTEXT_MESSAGES:]:
        parts.append(f"{role.upper()}: {text}\n")
    parts.append(f"USER: {user_input}\nASSISTANT:")
    return "\n".join(parts)

def generate_reply(prompt):
    resp = client.models.generate_content(
        model=MODEL,
        contents=prompt,
        config={
            "temperature": TEMPERATURE,
            "max_output_tokens": 1024
        }
    )
    
    return resp.text

def chat_loop():
    system_prompt = (
        "You are a helpful, concise assistant. Provide clear answers; when unsure, say you don't know. "
        "Prefer short step-by-step instructions when asked."
    )
    history = []  
    print("Chatbot ready — type 'quit' to exit.")
    while True:
        user_input = input("\nYou: ")
        if user_input.strip().lower() in ("quit","exit"):
            break

        prompt = build_prompt(system_prompt, history, user_input)
        reply = generate_reply(prompt)

        
        history.append(("user", user_input))
        history.append(("assistant", reply))
        print("\nBot:", reply)

if __name__ == "__main__":
    chat_loop()