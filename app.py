from flask import Flask, render_template, request, jsonify
from chat_logic import generate_reply

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    reply = generate_reply(user_input)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
