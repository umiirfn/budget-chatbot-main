# app.py

import streamlit as st
import openai
import os
import time

# Load the OpenAI API key
api_key = st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("🚨 OpenAI API key not found. Please add it in Streamlit Secrets.")
    st.stop()

client = openai.OpenAI(api_key=api_key)

# Set up the Streamlit page
st.set_page_config(page_title="💬 BudgetBot", layout="centered")
st.markdown("<h1 style='text-align: center;'>💬 BudgetBot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Your friendly AI money buddy. Let’s talk spending, saving, and skint days — no shame here 💚</p>", unsafe_allow_html=True)
st.markdown("---")

# 🔘 Mode Selector
mode = st.radio("Choose a tone:", ["Default", "Student Mode", "Pensioner Mode"], horizontal=True)

if mode == "Student Mode":
    tone = "You're speaking to a young university student. Use casual language and emojis. Help them manage a tight student budget."
elif mode == "Pensioner Mode":
    tone = "You're speaking to a retired pensioner. Be extra kind, clear, and gentle. Help them with fixed income challenges."
else:
    tone = "You're BudgetBot — a warm, supportive AI that helps people talk about money in real, everyday ways."

# Store conversation in session
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": tone},
        {"role": "assistant", "content": "Hey there! 👋 I’m BudgetBot — your AI money mate. Want to talk about your budget, savings, or spending habits? 💸"}
    ]

# Show message bubbles
for msg in st.session_state.messages[1:]:
    if msg["role"] == "user":
        st.markdown(f"<div style='background-color:#e1f5fe; padding:10px; border-radius:10px; margin-bottom:10px;'><b>You:</b><br>{msg['content']}</div>", unsafe_allow_html=True)
    elif msg["role"] == "assistant":
        st.markdown(f"<div style='background-color:#f1f8e9; padding:10px; border-radius:10px; margin-bottom:10px;'><b>BudgetBot:</b><br>{msg['content']}</div>", unsafe_allow_html=True)

# Input area
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your message:", placeholder="e.g. I’m broke till payday or Can I afford a takeaway?")
    submit = st.form_submit_button("Send")

if submit and user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("BudgetBot is thinking..."):
        # Simulate typing animation
        time.sleep(0.5)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": tone}] + st.session_state.messages[1:],
            max_tokens=200,
            temperature=0.85
        )
        reply = response.choices[0].message.content.strip()
        st.session_state.messages.append({"role": "assistant", "content": reply})
