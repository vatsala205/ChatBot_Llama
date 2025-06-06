🧠 AI Coverage Assistant Chatbot
A locally hosted AI-powered chatbot designed to assist users with coverage, app features, and general support queries. Built using Flask and a lightweight local language model (via Ollama), the assistant serves responses in a focused, helpful tone.

🚀 Features
🗣️ Natural language understanding via local LLM

📡 Domain-specific prompt tuning for relevant responses

💬 Clean and simple web-based chat interface

🔒 Fully local – no external API calls

🛠 Tech Stack
Python (Flask)

JavaScript (vanilla)

HTML/CSS

Ollama (for running LLMs locally)

📦 Setup Instructions
Clone the repository

git clone https://github.com/your-username/ai-coverage-chatbot.git
cd ai-coverage-chatbot/backend
Create and activate a virtual environment


python -m venv venv
venv\Scripts\activate   # Windows
Install dependencies

pip install flask
Run Ollama in a separate terminal


ollama serve
Run the Flask app


python app.py
Visit
Open http://127.0.0.1:5000 in your browser.

📂 Project Structure
**
chatbot_llama/
├── backend/
│   ├── app.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       ├── style.css
│       └── script.js
**

🤖 Prompt Template
All queries use this custom prompt format:
**
You are a helpful assistant for a coverage-based mobile app. Provide clear and concise answers to users about network coverage, availability, in-app functionality, and any related queries.
User: <message>
AI:
**
