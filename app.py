# app.py

import streamlit as st
import openai
import os

# Load the OpenAI API key
api_key = st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("🚨 OpenAI API key not found. Please add it in Streamlit Secrets.")
    st.stop()

client = openai.OpenAI(api_key=api_key)

# Streamlit page setup
st.set_page_config(page_title="💬 BudgetBot", layout="centered")

st.markdown("<h1 style='text-align: center;'>💬 BudgetBot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Your friendly AI money buddy. Let’s talk spending, saving, and skint days — no shame here 💚</p>", unsafe_allow_html=True)
st.markdown("---")

# Conversation history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": (
            "You are BudgetBot, a warm, supportive financial chatbot who helps people talk about money in real, everyday ways. "
            "You use casual language, emojis, and emotional intelligence to make people feel safe and supported. "
            "Help students, pensioners, and anyone struggling financially — without judgment."
        )},
        {"role": "assistant", "content": "Hey there! 👋 I’m BudgetBot — your AI money mate. Want to talk about your budget, savings, or spending habits? 💸"}
    ]

# Show chat messages
for msg in st.session_state.messages[1:]:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    elif msg["role"] == "assistant":
        st.markdown(f"**BudgetBot:** {msg['content']}")

# Input box with placeholder
user_input = st.text_input("Type your message:", placeholder="e.g. I'm broke till payday or Can I afford a takeaway?")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("BudgetBot is thinking..."):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.messages,
            max_tokens=200,
            temperature=0.85
        )

        reply = response.choices[0].message.content.strip()
        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.markdown(f"**BudgetBot:** {reply}")
