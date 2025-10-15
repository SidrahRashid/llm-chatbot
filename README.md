🌐 Gemini AI Chatbot (Web App)

A Python Flask web app powered by Google Gemini API, allowing real-time AI conversations through a browser. The chatbot is fully LLM-driven, preserves conversation context, and is accessible globally without exposing your API key.

🌟 Features
AI-driven conversations: No rules, JSON, or predefined flows — pure Gemini LLM responses.
Context memory: Remembers the last messages for coherent replies.
Web interface: Simple, interactive, and user-friendly.
Global access: Can be deployed on any server for worldwide usage.
Secure API handling: Gemini API key is never exposed to users.

⚙️ Technologies Used
Python 3.12+
Flask
 – Lightweight web framework
Google GenAI SDK
 – Gemini API integration
python-dotenv
 – Manage environment variables

💻 Installation
Clone the repository

git clone https://github.com/SidrahRashid/gemini-ai-chatbot-web.git
cd gemini-ai-chatbot-web

Create a virtual environment
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows


Install dependencies
pip install -r requirements.txt

Set up your Gemini API key


🚀 Run the Web App Locally
python app.py
Open a browser → http://127.0.0.1:5000

Start chatting with your Gemini AI chatbot.

🌐 How It Works

User input is entered in the web interface.
Flask backend sends input to Gemini API using the secure API key.
AI generates a context-aware response.
The response is displayed on the web page in real-time.
Conversation history is stored server-side, maintaining context across messages.

🔧 Configuration Options
Parameter	Description
MODEL	Gemini chat model (default: "gemini-2.5-flash")
TEMPERATURE	Controls creativity of responses (0 = deterministic, 1 = very creative)
MAX_CONTEXT_MESSAGES	Number of previous messages remembered for context

🔒 Security Notes

API key is never exposed to the browser or users.
Monitor API usage to prevent unexpected costs.

📈 Future Enhancements

Add user authentication for multiple users.
Integrate RAG (retrieval-augmented generation) for factual responses.
Deploy to Render / Heroku / AWS / GCP for full global access.
Improve UI with modern frontend frameworks like React or Vue.