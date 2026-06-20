# Banking GenAI Assistant

## Project Overview

Banking GenAI Assistant is an internal AI-powered assistant designed to help bank staff quickly retrieve accurate information from banking policy documents. Instead of manually searching through lengthy PDFs, users can ask questions in natural language and receive context-aware answers using Retrieval-Augmented Generation (RAG) and Large Language Models (LLMs).

## Problem Statement

Banking organizations maintain large volumes of policy documents, operational guidelines, and compliance manuals. Employees often spend considerable time searching through these documents to find relevant information. This project addresses this challenge by providing an AI-powered assistant that delivers instant, accurate, and context-aware answers from banking documents.

## Tech Stack

* **Frontend:** Streamlit
* **Programming Language:** Python 3.10
* **LLM:** LLaMA3 (Ollama)
* **Vector Database:** ChromaDB
* **Embeddings:** all-MiniLM-L6-v2 (HuggingFace)
* **Search:** Semantic Search + BM25 (rank-bm25)
* **Authentication:** bcrypt
* **Database:** SQLite

## Features

* Secure login with bcrypt password hashing
* PDF ingestion and indexing into ChromaDB
* Hybrid search combining Semantic Search and BM25 reranking
* Query expansion for common banking terms
* Role-based access control
* Chat history with timestamps
* Manager activity reports
* AI-powered question answering from banking policy documents

## Role-Based Access Control

### Admin

* Upload banking policy PDFs
* Delete uploaded PDFs
* View all user chat history

### Manager

* View clerk activity reports
* Add new clerks
* Ask banking-related questions

### Clerk

* Ask banking-related questions
* View personal chat history

## How to Run

### Prerequisites

* Python 3.10+
* Ollama installed with LLaMA3 model

### Installation

```bash
# Clone the repository
git clone https://github.com/hema37619-dot/banking-genai-assistant.git
cd banking-genai-assistant

# Create virtual environment
python -m venv myenv
myenv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Pull LLaMA3 model
ollama pull llama3
```

### Setup Database

```bash
python create_db.py
```

### Run the Application

```bash
streamlit run app.py
```

## Project Structure

```text
banking_genai_assistant/
├── app.py
├── config.py
├── create_db.py
├── auth/
│   ├── login.py
│   └── hash_password.py
├── rag/
│   ├── ingest.py
│   ├── retriever.py
│   ├── hybrid_search.py
│   └── llm.py
├── dashboard/
│   ├── admin.py
│   ├── clerk.py
│   └── manager.py
├── history/
│   └── chat_history.py
└── database/
    ├── users.db
    ├── chat_history.db
    └── chroma_db/
```

## Future Improvements

* Individual credentials for each employee
* Password expiry and reset functionality
* Date-based filtering in manager reports
* Support for multiple document formats
* Enhanced reporting and analytics
* Deployment as an internal web application

