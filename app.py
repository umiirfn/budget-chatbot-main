import openai
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

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

# User input
user_input = st.text_input("You:", key="input")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("BudgetBot is thinking..."):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=st.session_state.messages,
            max_tokens=200,
            temperature=0.85
        )
        reply = response.choices[0].message["content"]
        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.markdown(f"**BudgetBot:** {reply}")
