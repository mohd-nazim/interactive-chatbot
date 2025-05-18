from flask import Flask, request, jsonify, send_from_directory
import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Environment variables se load ho raha hai
GROQ_API_URL = os.getenv("GROQ_API_URL")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

@app.route('/')
def index():
    return "Server is running. Use the /chat endpoint to communicate."

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get('message', '')

    payload = {
        "model": "llama-3.3-70b-versatile",
        "prompt": user_input,
        "max_tokens": 512,
        "temperature": 0.7,
    }

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(GROQ_API_URL, json=payload, headers=headers)
    if response.status_code == 200:
        result = response.json()
        answer = result.get('result', '') 
        return jsonify({"answer": answer})
    else:
        return jsonify({"error": "Failed to get response from Groq API"}), 500
