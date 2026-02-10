
# Context-Aware Llama 3 Chatbot

A **context-aware chatbot** built using **LangChain** and **Ollama Llama 3** models, deployed via **Streamlit**.  
This chatbot remembers conversational context within a session and responds with a persona-driven style (e.g., acting like an astronaut).


---

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [System Requirements](#system-requirements)  
4. [Installation](#installation)  
5. [Usage](#usage)  
6. [Project Structure](#project-structure)  
7. [Future Enhancements](#future-enhancements)  
8. [Skills Gained](#skills-gained)  
9. [References](#references)  

---

## Project Overview

This project demonstrates a **context-aware AI chatbot** using the Llama 3.2 model via the **Ollama Python API**. The chatbot can:  

- Maintain conversational context using **Streamlit session state**  
- Respond according to a **custom persona** (e.g., astronaut)  
- Provide a **Streamlit web interface** for interactive chat  

It is designed as a foundation for more advanced **RAG-enabled chatbots**, where the model could retrieve knowledge from external documents or a custom corpus.  

---

## Features

- **Conversational Context Memory:** Stores all previous messages in the current session.  
- **Persona-driven Responses:** Use `SystemMessage` to instruct the AI to act as a specific persona.  
- **Interactive Web Interface:** Built with **Streamlit** for user-friendly chatting.  
- **Modular Code:** Python scripts separated for Llama interaction, Streamlit demo, and chat interface.  

---

## System Requirements

- **Operating System:** Windows 10/11 (or any OS supported by Streamlit and Ollama)  
- **Python Version:** 3.10+ recommended (tested with Python 3.13)  
- **Ollama:** Installed and configured with `llama3.2:1b` model  
- **Dependencies:** Installed via `pip` (see Installation)  
- **Hardware:** CPU (Intel i3+), SSD recommended; GPU optional for faster responses  

---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/Azharmunir96/context-aware-chatbot.git
cd "ollama chatbot"
````

2. **Create and activate a virtual environment (Windows PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. **Install required packages:**

```powershell
pip install streamlit langchain-ollama langchain_core
```

4. **Ensure Llama 3.2:1B model is installed via Ollama:**

```powershell
ollama pull llama3.2:1b
```

5. **Verify installed models:**

```powershell
ollama list
```

---

## Usage

1. **Run the Streamlit chatbot:**

```powershell
streamlit run 4_chatbot_ollama.py
```

2. **Open the browser URL** shown in the terminal (usually `http://localhost:8501`).

3. **Chat with the AI:**

* Type your message in the input bar.
* The AI responds according to its persona and remembers previous messages.
* Example system persona: `"Act like an astronaut"`.

---

## Project Structure

```
ollama chatbot/
│
├─ venv/                       # Virtual environment
├─ 1_python_ollama.py           # Python-only Llama 3 interaction demo
├─ 2_streamlit_example.py       # Basic Streamlit chat example
├─ 3_chatbot_echo.py            # Streamlit echo chatbot demo
├─ 4_chatbot_ollama.py          # Full context-aware Streamlit chatbot with Llama 3.2
├─ README.md                    # Project documentation
├─ requirements.txt             # Optional: list of Python dependencies
```

---

## Future Enhancements

* **Retrieval-Augmented Generation (RAG):**
  Integrate a vector store (FAISS, Chroma, Pinecone) to retrieve answers from a **custom knowledge base or Wikipedia corpus**.

* **Long-term memory:**
  Store conversations beyond a single session for continuous context.

* **Improved UI:**
  Add buttons for **predefined questions**, typing indicators, or visual themes.

* **Performance:**
  Use GPU for faster Llama responses and lower CPU load.

---

## Skills Gained

* **Conversational AI development** using LangChain and Llama
* **Session-based context memory** in Streamlit
* **LLM integration with Python**
* **Streamlit deployment for interactive apps**
* (Future) **Document embedding and RAG integration**


