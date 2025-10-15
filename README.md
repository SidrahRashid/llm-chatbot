📘 Gemini AI Chatbot

A Python-based AI chatbot powered by Google Gemini API, capable of free-text conversation without any rule-based logic or JSON formatting. This project demonstrates building a pure LLM-driven chatbot with conversation memory and a simple terminal interface.

🌟 Features

Pure AI-powered chatbot: No rule-based logic, JSON, or pre-defined flows.

Contextual memory: Remembers the last few messages for coherent conversations.

Configurable behavior: Adjust model, temperature, and response length.

Safe API usage: API key managed via environment variables; no hardcoding.

Lightweight terminal interface for fast testing.

Can be extended with RAG / embeddings for more factual answers.

⚙️ Technologies Used

Python 3.12+

Google GenAI SDK (google-genai)

Optional: python-dotenv for local environment variable management

💻 Installation

Clone the repository

git clone https://github.com/yourusername/gemini-ai-chatbot.git
cd gemini-ai-chatbot


Create a virtual environment (recommended)

python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows


Install dependencies

pip install -U google-genai
# optional: if using .env
pip install python-dotenv


Set up your Gemini API key

Option 1 (Environment Variable):

# Windows PowerShell
setx GEMINI_API_KEY "your_actual_api_key_here"

# Linux / Mac
export GEMINI_API_KEY="your_actual_api_key_here"


Option 2 (Using .env file):

Create a .env file in project root:

GEMINI_API_KEY=your_actual_api_key_here


Ensure .env is listed in .gitignore.

🚀 Usage

Run the chatbot script:

python chatbothf.py


Chat with the AI in your terminal:

Chatbot ready — type 'quit' to exit.

You: hi
Bot: Hello! How are you today?


To exit, type:

quit


or

exit

🔧 Configuration

You can customize the chatbot in chatbothf.py:

Variable	Description
MODEL	Gemini model to use (e.g., "gemini-2.0-flash")
TEMPERATURE	Controls creativity (0 = deterministic, 1 = creative)
MAX_CONTEXT_MESSAGES	Number of recent messages remembered for context
💡 How it works

The chatbot reads the system prompt (instructions for AI).

It constructs a prompt combining the system instruction + recent conversation + current user input.

Sends the prompt to Google Gemini API using the google-genai SDK.

Receives the AI-generated reply and prints it in the terminal.

Stores the conversation in memory to maintain context.

🔒 Security

Never hardcode your API key. Always use environment variables or .env.

Add .env to .gitignore to prevent accidental commits.

Monitor your API usage to avoid unexpected charges.

📈 Future Improvements

Add a web interface using Flask or FastAPI.

Integrate RAG (retrieval-augmented generation) for knowledge-based responses.

Add logging and session management for multiple users.

Add conversation summaries to reduce token usage.