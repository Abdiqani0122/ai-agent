# 🤖 AI Agent (Internet-Enabled, Local LLM)

This project is a **simple but structured AI agent** that answers user questions by **searching the internet** and reasoning over the results using a **local large language model (LLM)**.

It is designed to demonstrate **agent architecture**, not just a basic chatbot.

---

## ✨ Features

- ✅ Conversational CLI interface
- 🌐 Internet search using DuckDuckGo (`ddgs`)
- 🧠 Local LLM inference using **GPT4All**
- 🔍 Grounded answers based on search results
- 🧩 Modular agent design (tools, reasoning, model separated)
- ❌ No hard-coded questions or answers

---

## 🧠 The agent focuses on **doing one task well**:

### This is:
> Answering questions accurately using external information.


---

## 🏗️ Project Structure

```
ai-agent/
├── main.py              # CLI entry point
├── agent/
│   ├── agent.py         # Agent logic and decision flow
│   ├── tools.py         # Tools (web search, summarization)
│   ├── local_llm.py     # Local LLM (GPT4All) interface
├── memory.json          # Lightweight memory (optional)
├── requirements.txt
└── README.md
```


