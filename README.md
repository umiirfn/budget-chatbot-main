# 💬 Budget Chatbot

A friendly, emotionally intelligent chatbot that helps you talk about money in real-life language (like “I’m skint till Friday”) and feel better about your finances. Built with Python + AI.

---

## 🌟 Features

- Understands everyday money talk and slang (e.g. *"I'm broke"*, *"Can I afford a takeaway?"*)
- Friendly, empathetic responses with emojis 😊
- Works in terminal **or** with a clean web interface
- Rule-based version for offline use 💻
- GPT-powered version for smarter replies 🧠
- Streamlit app for chatting in your browser 🖥️

---

## 🧠 How It Works

You can run this chatbot in **three ways**:

### ✅ 1. Basic Rule-Based Chatbot (Offline)

File: `chatbot.py`

> Best for quick demos without AI or internet.

```bash
python chatbot.py
```

---

### 🤖 2. AI-Powered Chatbot in Terminal (OpenAI GPT)

File: `chatbot_ai.py`

> Uses OpenAI's GPT-4 to give human-like, emotionally aware replies.

```bash
python chatbot_ai.py
```

✅ Requires a `.env` file with your OpenAI API key  
✅ Internet connection needed

---

### 💬 3. Streamlit Web Chat App

File: `app.py`

> Launches a web-based chat interface with Streamlit.

```bash
streamlit run app.py
```

✅ Requires `.env` file with API key  
✅ Great for showcasing or demoing your chatbot

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/budget-chatbot.git
cd budget-chatbot
```

### 2. Create Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Add Your `.env` File (Do Not Upload This!)

Create a `.env` file in the root of the project:

```env
OPENAI_API_KEY=sk-your-openai-key-here
```

Your `.gitignore` will make sure this file stays private 🔒

---

## 📦 Project Structure

```
budget-chatbot/
├── chatbot.py           ← Basic rule-based chatbot
├── chatbot_ai.py        ← GPT-powered terminal chatbot
├── app.py               ← Streamlit web app
├── requirements.txt     ← Project dependencies
├── .env                 ← Your secret API key (DO NOT UPLOAD)
├── .gitignore           ← Hides .env and cache files
└── README.md            ← You’re reading it!
```

---

## 🔮 Future Plans

- Add CSV import for tracking real spending
- Weekly check-ins with budgeting suggestions
- Deploy to Streamlit Cloud for public access
- Voice-to-text input and smart reminders
- Create student- and pensioner-focused versions

---

## ✨ Credits

Built by **Umar** as part of a GitHub portfolio to explore **empathetic AI for personal finance**.  
Let’s talk money — the human way 💬💚
