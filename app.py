# app.py

import openai
import streamlit as st
import os
from dotenv import load_dotenv

# Load the API key from secrets or .env fallback
api_key = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else os.getenv("OPENAI_API_KEY")

client = openai.OpenAI(api_key=api_key)

st.set_page_config(page_title="💬 BudgetBot", layout="centered")
st.title("💬 BudgetBot")
st.markdown("Your friendly AI money buddy. Type your thoughts, questions, or worries 💸")

# Store conversation
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": (
            "You are BudgetBot, a warm, supportive financial chatbot who helps people talk about money in real, everyday ways. "
            "You speak casually, use emojis to lighten tough topics, and tailor your tone depending on the user's situation. "
            "Always reply in a friendly, encouraging way, and make sure they feel heard and understood. Include emojis in your responses."
        )}
    ]

# Input box
user_input = st.text_input("You:", key="input")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("BudgetBot is thinking..."):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.messages,
            max_tokens=200,
            temperature=0.85
        )

        reply = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.markdown(f"**BudgetBot:** {reply}")
