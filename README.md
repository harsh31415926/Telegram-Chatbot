# 🚀 HarshBot – LLM-Powered Telegram Assistant

An intelligent Telegram bot powered by **Groq’s LLaMA 3.3 70B model**, built using **LangChain** and **Aiogram**.  
Designed for real-time, context-aware conversations with a scalable and production-ready backend.

---

## ✨ Features

- 🤖 AI-powered real-time chat  
- 💬 Conversation memory for contextual replies  
- ⚡ Async architecture using Aiogram  
- 🧹 `/clear` command to reset chat history  
- 🛠️ Multiple commands: `/start`, `/help`, `/info`, `/personal`  
- 🐳 Docker support for easy deployment  

---

## 🧠 Tech Stack

- **Python**
- **Aiogram**
- **LangChain**
- **Groq API (LLaMA 3.3 70B)**
- **Docker**
- **python-dotenv**

---

## ⚙️ Setup

### 1. Clone the repository
```bash```
git clone <your-repo-link>
cd <your-repo-name>

conda create -n telebot python=3.8 -y
conda activate telebot

pip install -r requirements.txt

# Architecture

User (Telegram)
      ↓
Aiogram Bot (Async Handler)
      ↓
LangChain
      ↓
Groq LLM (LLaMA 3.3 70B)
      ↓
Response → Telegram
