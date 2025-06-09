import os
from flask import Flask, render_template, request, jsonify, session
import cohere
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
# Set Flask secret key from environment variable (fallback only used for local dev)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "e67e0d7cc234cbcf0cb56936a26302581178ac75d5b5e45d4b937bcaec3475a9")

# Read Cohere API key from environment variable
cohere_api_key = os.getenv("COHERE_API_KEY")
if not cohere_api_key:
    raise ValueError("⚠️ COHERE_API_KEY environment variable not set!")
co = cohere.Client("cohere_api_key")  # Replace with your API key

# Rate Limiter config (5 requests per minute per IP)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["5 per minute"]
)
@app.route('/')
def index():
    session['chat_history'] = []
    return render_template("index.html")

@app.route('/ask', methods=['POST'])
@limiter.limit("5 per minute")   # Apply limit on this endpoint
def ask():
    user_message = request.json['message']
    # Get previous chat history (up to last 5 exchanges)
    history = session.get('chat_history', [])

    # Create context prompt for Cohere
    prompt = ""
    for turn in history[-5:]:
        prompt += f"User: {turn['user']}\nBot: {turn['bot']}\n"
    prompt += f"User: {user_message}\nBot:"

    response = co.generate(
        model='command-r-plus',  # You can also try command-xlarge
        prompt=user_message,
        max_tokens=300,
        temperature=0.7
    )
    bot_reply = response.generations[0].text.strip()
    # Update session history
    history.append({'user': user_message, 'bot': bot_reply})
    session['chat_history'] = history
    return jsonify({'reply': bot_reply})

if __name__ == '__main__':
    app.run(debug=True)
