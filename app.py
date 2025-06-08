import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

port = int(os.environ.get("PORT", 8000))  # Elastic Beanstalk sets this to 8000

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return "App is running!"

@app.route('/generate-persona', methods=['POST'])
def generate_persona():
    data = request.json
    user_input = data.get('text')

    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    prompt = f"""
    Based on the following customer review or transcript, generate a detailed user persona including:
    - Demographics
    - Goals
    - Pain points
    - Personality traits
    - Preferred communication style

    Text:
    \"\"\"{user_input}\"\"\"
    """

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=500
        )
        result = response.choices[0].message.content
        return jsonify({"persona": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
