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