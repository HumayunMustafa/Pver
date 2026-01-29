# PDF Retrieval with RAG

A Python-based PDF question-answering system using Retrieval-Augmented Generation (RAG) with LangChain and OpenAI.

## Overview

This project allows you to ask questions about PDF documents without manually searching through them. It uses LLM technology with RAG to retrieve relevant information and provide accurate answers.

**Status:** Work in progress. Currently supports terminal-based interaction only.

## Features

- PDF document processing and chunking
- Vector embeddings using OpenAI
- FAISS vector store for efficient similarity search
- Persistent caching of embeddings on disk
- Interactive question-answering interface
- Command-line interface

## Prerequisites

- Python 3.11 or higher
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd PDFRetrieval
```

2. Create and activate a virtual environment:
```bash
python3 -m venv rag_venv
source rag_venv/bin/activate  # On Mac/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

### Basic Usage

Run the program with a PDF file:
```bash
python main.py --doc_path /path/to/your/document.pdf
```

### First Run vs Subsequent Runs

**First run:** Creates embeddings and saves them to disk (may take 10-30 seconds depending on PDF size)
```bash
python main.py --doc_path /Users/documents/example.pdf
```

**Subsequent runs:** Loads embeddings from disk (near-instant, <1 second)
```bash
python main.py --doc_path /Users/documents/example.pdf
```

### Force Recreate

If your PDF has been updated, force recreation of the vectorstore:
```bash
python main.py --doc_path /path/to/document.pdf --recreate
```

### Interactive Mode

Once running, you can ask questions about the PDF:
```
Alright ask question related to pdf you shared
> What is the main topic of this document?

******************************
LLM Result: 
The main topic of this document is...
******************************

Press q to exit
```

Type `q` to exit the program.

## Project Structure

```
PDFRetrieval/
├── main.py                 # Entry point
├── src/
│   ├── embeddings.py      # PDF processing and embedding creation
│   └── chat.py            # Question-answering chain setup
├── vectorstore_*/         # Cached embeddings (auto-generated)
├── .env                   # API keys (not tracked)
├── .gitignore
└── README.md
```

## How It Works

1. **Document Loading:** Loads PDF using PyPDFLoader
2. **Chunking:** Splits document into chunks (1000 chars with 200 char overlap)
3. **Embedding:** Creates vector embeddings using OpenAI embeddings
4. **Storage:** Saves embeddings to disk using FAISS for future use
5. **Retrieval:** Retrieves top 4 most relevant chunks for each query
6. **Generation:** Uses OpenAI LLM to generate answers based on retrieved context

## Configuration

Key parameters in `embeddings.py`:
- `chunk_size`: 1000 characters
- `chunk_overlap`: 200 characters

Key parameters in `main.py`:
- `search_kwargs["k"]`: 4 (number of chunks to retrieve)

## Notes

- Vectorstores are cached on disk in `vectorstore_<filename>/` folders
- Each PDF gets its own vectorstore based on the filename
- Vectorstores are excluded from git via `.gitignore`
- First-time processing requires OpenAI API calls; subsequent loads are instant

## Future Enhancements

- Web interface
- Support for multiple document formats
- Batch processing
- Advanced retrieval strategies
- Conversation history

## Author

Created by Humayun Mustafa on 29 January 2026

## License

[Add your license here]
