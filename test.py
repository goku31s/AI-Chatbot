from google import genai
from google.genai import types

PROJECT_ID = "abhinav-project-469317"
LOCATION = "us-central1"  # use a region, not "global"
MODEL = "gemini-2.5-flash-lite"

# Create client
client = genai.Client(
    vertexai=True,
    project=PROJECT_ID,
    location=LOCATION,
)

def run_chat():
    print("Chatbot ready. Type 'exit' to quit.\n")

    # Conversation history
    history = []

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        # Add user message to history
        history.append(
            types.Content(role="user", parts=[types.Part(text=user_input)])
        )

        # Send full history each time (Gemini remembers conversation)
        response = client.models.generate_content(
            model=MODEL,
            contents=history,
            config=types.GenerateContentConfig(
                temperature=0.7,
                max_output_tokens=512,
                top_p=0.95,
            ),
        )

        # Get AI reply
        ai_reply = response.candidates[0].content.parts[0].text
        print(f"AI: {ai_reply}\n")

        # Save AI reply to history
        history.append(
            types.Content(role="model", parts=[types.Part(text=ai_reply)])
        )

if __name__ == "__main__":
    run_chat()
