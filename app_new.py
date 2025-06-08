import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import openai
import csv
from io import StringIO
import pandas as pd  # Add pandas for Excel file handling
import logging

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

port = int(os.environ.get("PORT", 8000))  # Elastic Beanstalk sets this to 8000

app = Flask(__name__)
CORS(app)

logging.basicConfig(level=logging.INFO)

@app.route('/', methods=['GET'])
def home():
    return "App is running!"

def generate_persona_from_text(user_input):
    sanitized_input = user_input.replace('"', '\\"')  # Escape quotes
    prompt = f"""
    Based on the following customer review or transcript, generate a detailed user persona including:
    - Demographics
    - Goals
    - Pain points
    - Personality traits
    - Preferred communication style

    Text:
    \"\"\"{sanitized_input}\"\"\"
    """
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=500
    )
    return response.choices[0].message.content

@app.route('/generate-persona', methods=['POST'])
def generate_persona():
    data = request.json
    user_input = data.get('text')

    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    try:
        result = generate_persona_from_text(user_input)
        return jsonify({"persona": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/generate-personas-batch", methods=["POST"])
def generate_personas_batch():
    try:
        data = request.get_json()
        if not data or not isinstance(data, list):
            return jsonify({"error": "Invalid input format. Expected a JSON array."}), 400

        required_keys = {"customer_id", "review"}
        for item in data:
            if not required_keys.issubset(item.keys()):
                return jsonify({"error": "JSON data is missing required keys: 'customer_id' and 'review'"}), 400

        results = []
        for item in data:
            customer_id = item.get("customer_id")
            review = item.get("review")

            if not customer_id or not review:
                continue  # Skip invalid rows

            try:
                persona = generate_persona_from_text(review)
            except Exception as e:
                persona = f"Error: {str(e)}"

            results.append({
                "Customer ID": customer_id,
                "Review": review,
                "Persona": persona
            })

        return jsonify({"status": "success", "data": results}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/generate-personas-batch-csv", methods=["POST"])
def generate_personas_batch_csv():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    try:
        # Log file details
        logging.info(f"Processing file: {file.filename}")

        # Determine file type and parse accordingly
        if file.filename.endswith('.csv'):
            stream = StringIO(file.stream.read().decode("utf-8"))
            reader = csv.DictReader(stream)
            data = list(reader)
            if not data:
                return jsonify({"error": "The uploaded CSV file is empty or invalid"}), 400
        elif file.filename.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(file)
            data = df.to_dict(orient="records")
            if df.empty:
                return jsonify({"error": "The uploaded Excel file is empty or invalid"}), 400
        else:
            return jsonify({"error": "Unsupported file type. Please upload a CSV or Excel file."}), 400

        # Validate required keys
        required_keys = {"customer_id", "review"}
        for item in data:
            if not required_keys.issubset(item.keys()):
                logging.warning("File is missing required columns")
                return jsonify({"error": "File is missing required columns: 'customer_id' and 'review'"}), 400

        # Process the parsed data
        results = []
        for item in data:
            customer_id = item.get("customer_id")
            review = item.get("review")

            if not customer_id or not review:
                continue  # Skip invalid rows

            try:
                persona = generate_persona_from_text(review)
            except Exception as e:
                persona = f"Error: {str(e)}"

            results.append({
                "Customer ID": customer_id,
                "Review": review,
                "Persona": persona
            })

        return jsonify({"status": "success", "data": results}), 200
    except Exception as e:
        logging.error(f"Error processing file: {str(e)}")
        return jsonify({"error": str(e)}), 500



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
