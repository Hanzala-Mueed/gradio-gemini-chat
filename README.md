# Semantic PDF Assistant

A semantic PDF-based AI assistant built with Gradio, Gemini, and Retrieval-Augmented Generation (RAG) concepts.

The application reads PDF documents, creates semantic embeddings, retrieves the most relevant content using cosine similarity, and answers user questions based only on the document context.

---

## Features

### Authentication
- Simple login authentication
- Default credentials:
  - Username: `user`
  - Password: `123`

### AI Chatbot
- Gemini-powered chatbot
- Custom system prompts
- Context-aware responses

### PDF Processing
- Automatic PDF loading
- PDF text extraction using PyPDF
- Hardcoded document support

### Semantic Retrieval
- Document chunking
- Overlapping chunks
- Sentence Transformer embeddings
- Semantic similarity search
- Cosine similarity ranking

### RAG Pipeline
- User query embedding generation
- Retrieval of top relevant chunks
- Context injection into Gemini prompt
- Answers generated only from retrieved document context

### Logging & Error Handling
- Structured logging
- Custom exception classes
- Try/Except handling throughout the application

---

## Tech Stack

### Frontend
- Gradio

### Backend
- Python 3.11.9

### LLM
- Gemini 2.5 Flash

### Embeddings
- Sentence Transformers
- all-MiniLM-L6-v2

### Retrieval
- Cosine Similarity
- Scikit-Learn

### PDF Processing
- PyPDF

---

## Project Architecture

```text
User Question
      │
      ▼
Query Embedding
      │
      ▼
Cosine Similarity Search
      │
      ▼
Top Relevant Chunks
      │
      ▼
Gemini
      │
      ▼
Final Answer
```

---

## Project Structure

```text
semantic-pdf-assistant/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
│
├── auth/
│   └── login.py
│
├── config/
│   ├── prompts.py
│   └── settings.py
│
├── docs/
│   └── english2.pdf
│
├── document_loader/
│   ├── pdf_reader.py
│   └── chunking.py
│
├── llm/
│   ├── gemini_client.py
│   ├── embeddings.py
│   └── semantic_search.py
│
├── services/
│   ├── chat_service.py
│   └── document_service.py
│
├── ui/
│   └── gradio_ui.py
│
└── utils/
    ├── logger.py
    ├── exceptions.py
    └── helpers.py
```

---

## RAG Workflow

### Step 1 - Load PDF

```text
PDF
 ↓
Extract Text
```

### Step 2 - Chunking

```text
Document Text
 ↓
Overlapping Chunks
```

Example:

```text
Chunk 1: 0 - 500
Chunk 2: 400 - 900
Chunk 3: 800 - 1300
```

### Step 3 - Embeddings

```text
Chunks
 ↓
Sentence Transformer
 ↓
Vector Embeddings
```

### Step 4 - Semantic Search

```text
User Question
 ↓
Question Embedding
 ↓
Cosine Similarity
 ↓
Top 3 Relevant Chunks
```

### Step 5 - Answer Generation

```text
Relevant Chunks
 ↓
Gemini
 ↓
Final Response
```

---

## Installation

### 1. Clone Repository

```bash
git clone <repo-link>

```

---

### 2. Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root directory.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
MODEL_NAME=gemini-2.5-flash
```

---

## Getting Gemini API Key

1. Open Google AI Studio
2. Create an API Key
3. Copy the generated key
4. Paste it into `.env`

Google AI Studio:

https://aistudio.google.com/app/apikey

---

## Configure PDF

Place your PDF inside:

```text
docs/
```

Example:

```text
docs/
└── english2.pdf
```

Update PDF path if needed:

```python
services/chat_service.py
PDF_PATH = "docs/english2.pdf"
```

---

## Run Application

```bash
python app.py
```

Application starts on:

```text
http://127.0.0.1:7860
```

---

## Login Credentials

Default credentials:

```text
Username: user
Password: 123
```

---

## Example Questions

```text
What is a present perfect tense?

Explain examples of present perfect tense.

What are the rules of simple present tense?
```

---

## Current Limitations

- Single PDF support
- No vector database
- Embeddings generated at startup
- No PDF upload from UI
- No chat history persistence

---

## Future Improvements

### Version 3

- Multiple PDF support
- PDF upload from UI
- Embedding caching
- FAISS integration
- ChromaDB integration
- Conversation memory
- Streaming responses
- User management
- Document management dashboard

---

## Learning Concepts Covered

- Gradio UI
- Authentication
- Gemini API
- PDF Parsing
- Chunking
- Overlapping Chunking
- Embeddings
- Semantic Search
- Cosine Similarity
- Retrieval-Augmented Generation (RAG)
- Logging
- Exception Handling

---

## Author

Hanzala Mueed Khan

Semantic PDF Assistant – Vol 2