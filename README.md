# Sarva AI Autoreply Bot

A lightweight Python automation tool that monitors WhatsApp Desktop for new messages, captures conversation history, and automatically generates natural, context-aware humanized replies using the Groq API (powered by open-weight LLMs).

---

## Features

* **GUI Automation:** Uses PyAutoGUI to interact with WhatsApp Desktop safely.
* **Clipboard Extraction:** Captures active chat text dynamically using Pyperclip.
* **Smart State Tracking:** Tracks the last processed message to prevent duplicate automated responses.
* **Context-Aware Responses:** Configured via custom system prompts to respond as "Akhil" in natural English, Hinglish, or Kanglish.
* **Safety Fail-Safe:** Built-in PyAutoGUI fail-safe (moving mouse to any screen corner immediately stops execution).

---

## Tech Stack & Libraries

* **Language:** Python 3.x
* **GUI & Mouse Automation:** pyautogui
* **Clipboard Operations:** pyperclip
* **API Engine:** groq (LLM completion engine)

---

## Quickstart Guide

```bash
# 1. Clone the repository
git clone [https://github.com/akhileshshetti2/Sarva-AI-Autoreply-Bot.git](https://github.com/akhileshshetti2/Sarva-AI-Autoreply-Bot.git)
cd Sarva-AI-Autoreply-Bot

# 2. Install dependencies
pip install pyautogui pyperclip groq

# 3. Set your API key in your environment (recommended)
export GROQ_API_KEY="your-groq-api-key"

# 4. Run the auto-reply bot from your terminal
python main.py


Interaction Flow
Open WhatsApp Desktop and ensure the target chat window is visible.
Run main.py in your terminal.
The script periodically checks for new incoming messages, generates an AI response, and pastes it into the chat window automatically.
Move your mouse cursor to any corner of the screen or press Ctrl+C in terminal to stop execution.

Future Enhancements
Replace coordinate-based GUI clicks with direct WhatsApp Web API or selenium browser automation.
Load API credentials securely using python-dotenv.
Add custom contact filtering to only auto-reply to specific senders.
