# Chatbot_with_API

# AI Chatbot with RAG, Cohere API, and Voice Support

An intelligent AI chatbot built using **Python (Flask)**, **Cohere API**, **Retrieval-Augmented Generation (RAG)**, and **voice input/output** capabilities. It also features a dynamic frontend using **HTML, CSS, and JavaScript**, and is deployed on **Railway**.

---

## Features

- **RAG (Retrieval-Augmented Generation)** for answering from personal/project knowledge base
- **Cohere API** for natural language generation
- **Speech-to-Text** input using Web Speech API
- **Text-to-Speech** output
- **Frontend** with HTML, CSS, JS integrated with Flask backend
- **Deployed on Railway**

------------------------------------------------------------------------------------------------
## Project Structure

project-root/
│
├── static/
│ ├── style.css
│ └── script.js
├── templates/
│ └── index.html
├── data/
│ └── docs.txt / vector_store.pkl (your knowledge base)
├── app.py # Flask server
├── rag_utils.py # RAG logic using Cohere + embeddings
├── requirements.txt
└── README.md

1. **CREATE VIRTUAL ENVIRONMENT**
   python -m venv venv
   # For Windows: venv\Scripts\activate
   
2. **INSTALL DEPENDENCIES**
   pip install -r requirements.txt

3. **ADD YOUR COHERE API KEY**
   COHERE_API_KEY = "your_cohere_api_key_here"

4. **RUN THE APPLICATION**
   python app.py
-----------------------------------------------------------------------------------------------

**How RAG Works in This Project**
1.Text documents are converted into embeddings using Cohere.

2.When a user sends a query:
    The app retrieves relevant chunks from the knowledge base using vector similarity.
    The selected context is passed to the Cohere API for final answer generation.
    
**Voice Support**
Speech-to-Text: Uses browser's Web Speech API for real-time voice input.

**Deployment**
This project is deployed using Railway. You can fork and deploy it in minutes.
