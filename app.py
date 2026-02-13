from flask import Flask, render_template, request, jsonify
from google import genai
from google.genai import types

app = Flask(__name__)

# Config
PROJECT_ID = "abhinav-project-469317"
LOCATION = "us-central1"
MODEL = "gemini-2.5-flash-lite"

# Create GenAI client
client = genai.Client(
    vertexai=True,
    project=PROJECT_ID,
    location=LOCATION,
)

# Conversation history per session (global for simplicity)
history = []

# Generate AI response
def generate_response(user_input: str) -> str:
    # Add user input to conversation history
    history.append(types.Content(role="user", parts=[types.Part(text=user_input)]))

    # Generate response using GenAI
    response = client.models.generate_content(
        model=MODEL,
        contents=history,
        config=types.GenerateContentConfig(
            temperature=0.7,
            max_output_tokens=512,
            top_p=0.95,
        ),
    )

    # Extract AI reply
    ai_reply = response.candidates[0].content.parts[0].text

    # Save AI reply to conversation history
    history.append(types.Content(role="model", parts=[types.Part(text=ai_reply)]))

    return ai_reply

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    # Get user input
    user_input = request.args.get('user_input', "") if request.method == 'GET' else request.form.get('user_input', "")

    if not user_input:
        return jsonify(content="⚠️ No input provided.")

    # Generate AI response
    content = generate_response(user_input)
    return jsonify(content=content)

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
