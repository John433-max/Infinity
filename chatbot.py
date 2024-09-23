
from flask import Flask, request, jsonify
import joblib
import openai
import os

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.joblib')

# Set OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = data['features']
    prediction = model.predict([features])
    return jsonify({'prediction': prediction.tolist()})

@app.route('/code', methods=['POST'])
def generate_code():
    data = request.json
    prompt = data['prompt']
    print(f"Prompt: {prompt}")
    response = openai.completions.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    code = response.choices[0].text.strip()
    return jsonify({'code': code})

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    prompt = data['prompt']
    response = openai.completions.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    message = response.choices[0].text.strip()
    return jsonify({'message': message})

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
