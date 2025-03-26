# app.py

import streamlit as st
import openai
import os
import time

# ✅ Page config must come FIRST
st.set_page_config(page_title="💬 BudgetBot", layout="centered")


# Load the OpenAI API key
api_key = st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("🚨 OpenAI API key not found. Please add it in Streamlit Secrets.")
    st.stop()

client = openai.OpenAI(api_key=api_key)

# Theme Toggle
theme = st.toggle("🌗 Toggle Dark Mode")

# Set Page Config
st.set_page_config(page_title="💬 BudgetBot", layout="centered")
st.markdown(f"""
    <h1 style='text-align: center; color: {"white" if theme else "black"};'>💬 BudgetBot</h1>
    <p style='text-align: center; font-size: 18px; color: {"#cccccc" if theme else "#333"}'>
        Your friendly AI money mate. Pick a mode, ask anything, no shame here 💚
    </p>
    <hr style='border: none; height: 1px; background-color: {"#444" if theme else "#ccc"}'>
""", unsafe_allow_html=True)

# Mode Selector
mode = st.selectbox("Choose a mode:", [
    "🧑‍🎓 Student",
    "👵 Pensioner",
    "👔 Full-Time Worker",
    "📦 Sole Trader",
    "⚙️ Default"
])

if mode == "🧑‍🎓 Student":
    tone = "You're speaking to a university student on a tight budget. Use casual, emoji-filled, student-friendly language. Be relatable."
elif mode == "👵 Pensioner":
    tone = "You're speaking to a retired pensioner. Be respectful, simple, and gentle. Help with fixed income, bills, and peace of mind."
elif mode == "👔 Full-Time Worker":
    tone = "You're helping a full-time employee. Offer budgeting tips for salary, travel, savings, and handling bills efficiently."
elif mode == "📦 Sole Trader":
    tone = "You're advising a self-employed sole trader. Talk about taxes, inventory, stock costs, profits, and smart business money tips."
else:
    tone = "You're BudgetBot — a warm, supportive AI that helps people talk about money without judgment."

# Start the conversation
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": tone},
        {"role": "assistant", "content": "Hey there! 👋 I’m BudgetBot — your AI money mate. Let’s talk budgeting, saving, or business costs 💸"}
    ]

# Message Renderer (with avatars + themes)
def render_msg(role, content):
    if role == "user":
        bg = "#cce5ff" if not theme else "#2b3e50"
        text = "#003366" if not theme else "#dceeff"
        avatar = "🧑‍💻"
        label = "You"
    else:
        bg = "#e6ffe6" if not theme else "#344d2f"
        text = "#0b3d0b" if not theme else "#d4ffd4"
        avatar = "🤖"
        label = "BudgetBot"

    st.markdown(f"""
    <div style='background-color: {bg}; color: {text}; padding: 14px; border-radius: 12px; margin-bottom: 12px; font-size: 16px;'>
        <strong>{avatar} {label}:</strong><br>{content}
    </div>
    """, unsafe_allow_html=True)

# Display chat
for msg in st.session_state.messages[1:]:
    render_msg(msg["role"], msg["content"])

# Input form
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your message:", placeholder="e.g. Can I afford a takeaway?")
    submitted = st.form_submit_button("Send")

if submitted and user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("BudgetBot is thinking..."):
        time.sleep(0.4)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": tone}] + st.session_state.messages[1:],
            max_tokens=300,
            temperature=0.85
        )
        reply = response.choices[0].message.content.strip()
        st.session_state.messages.append({"role": "assistant", "content": reply})
