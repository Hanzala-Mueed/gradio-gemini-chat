# gradio-gemini-chat
An authentication-secured RAG chatbot template built with Gradio and Gemini API, supporting document context parsing and system prompt configuration.

gradio-gemini-chat/
│
├── app.py                     # Main entry point
├── requirements.txt
├── .env
├── README.md
│
├── config/
│   ├── settings.py            # API keys & configs
│   └── prompts.py             # System prompts
│
├── auth/
│   └── login.py               # Simple authentication logic
│
├── docs/
│   └── sample.pdf             # Hardcoded PDF
│
├── llm/
│   ├── gemini_client.py       # Gemini API handling
│   └── chatbot.py             # Chat response pipeline
│
├── document_loader/
│   └── pdf_reader.py          # Read PDF text
│
├── ui/
│   └── gradio_ui.py           # Gradio frontend
│
├── services/
│   └── chat_service.py        # Connect PDF + Prompt + Gemini
│
└── utils/
    └── helpers.py


## Gradio-Gemini-Chat

A simple AI-powered PDF chatbot built using:

- Gradio
- Gemini API
- Python
- PDF Reader

The chatbot reads a hardcoded PDF document and answers user questions according to the document content.

---

# 1. Clone the github repo
# 2. Create .venv and run this command
    pip install -r requirements.txt

# 3. create .env file in the project root dir and add these lines
    GEMINI_API_KEY=your_actual_gemini_api_key
    MODEL_NAME=gemini-2.5-flash

# 4. add pdf doc in docs/ and pdf filename should be like 'sample.pdf'
# 5. Run project by using this command : python app.py
# 6. sample login credentials 
    Username: user
    Password: 123

# Current Features (Vol 1)
    Gradio UI
    Login Authentication
    Gemini API Integration
    Hardcoded PDF Reading
    System Prompt Based Responses
    PDF Question Answering

# Current Limitations
    No chunking
    No embeddings
    No semantic retrieval
    No vector database
    Works best with text-based PDFs

# Upcoming Features (Vol 2)
    Chunking
    Embeddings
    Semantic Search
    Retrieval Pipeline
    Better Prompt Engineering
    Multiple PDF Support
