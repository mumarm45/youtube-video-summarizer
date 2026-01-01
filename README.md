# YouTube Summarizer

A Python application that summarizes YouTube videos and answers questions about video content using AI.

## Features

- **Video Summarization**: Automatically generate concise summaries of YouTube video transcripts
- **Q&A**: Ask questions about video content and get AI-powered answers using RAG (Retrieval-Augmented Generation)
- **Web Interface**: User-friendly Gradio interface for easy interaction

## Requirements

- Python 3.12+
- Anthropic API key

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd youtube-summerizer
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On macOS/Linux
```

3. Install dependencies:
```bash
uv pip install -e .
```

4. Create a `.env` file with your configuration:
```env
ANTHROPIC_API_KEY=your-api-key-here
ANTHROPIC_MODEL_ID=claude-3-5-haiku-20241022
TEMPERATURE=0.7
MAX_NEW_TOKENS=1024
```

## Usage

### Run the Web App

```bash
python main.py
```

The Gradio interface will launch at `http://localhost:7860`.

### Summarize a Video (CLI)

```bash
python src/sumerize_video.py
```

### Ask Questions About a Video (CLI)

```bash
python src/qa_agent.py
```

## Project Structure

```
youtube-summerizer/
├── main.py                     # Entry point for the web app
├── src/
│   ├── sumerize_video.py       # Video summarization logic
│   ├── qa_agent.py             # Q&A agent logic
│   └── modules/
│       ├── video_data_extract.py   # YouTube transcript extraction
│       ├── llm_model.py            # Anthropic LLM setup
│       ├── embedding_model.py      # HuggingFace embeddings
│       ├── langchain_data.py       # Text chunking & FAISS indexing
│       ├── prompts.py              # Prompt templates
│       ├── retriever.py            # RAG retrieval logic
│       └── presentaion.py          # Gradio UI
├── pyproject.toml
└── .env
```

## Tech Stack

- **LLM**: Anthropic Claude (via LangChain)
- **Embeddings**: HuggingFace sentence-transformers
- **Vector Store**: FAISS
- **UI**: Gradio
- **Transcript API**: youtube-transcript-api

## Sample 

<img width="1535" height="717" alt="image" src="https://github.com/user-attachments/assets/5ee97b5e-6f17-4698-ba23-87978921ad43" />

  
