# chatbot_ai.py

import os
import openai
from dotenv import load_dotenv

# ✅ Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# ✅ Create OpenAI client with new API
client = openai.OpenAI(api_key=api_key)

print("💬 BudgetBot (AI): Hello! Let’s chat about money in a real, human way. Type 'exit' to leave.")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() in ["exit", "bye", "quit"]:
        print("BudgetBot: Take care! Hope your money feels a little lighter 💚")
        break

    # ✅ New method for chat completion (OpenAI ≥ v1.0)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": (
                "You are BudgetBot, a warm, supportive financial chatbot who helps people talk about money in real, everyday ways. "
                "You use casual language, emojis, and emotional intelligence to make people feel safe and supported. "
                "Help students, pensioners, people with debt, and anyone feeling broke. Always be encouraging."
            )},
            {"role": "user", "content": user_input}
        ],
        max_tokens=200,
        temperature=0.85
    )

    print(f"BudgetBot: {response.choices[0].message.content}")