# RECALL

RECALL is a local-first desktop search application for finding information across your own files. The project begins with reliable local document ingestion and keyword search, then grows into semantic search and locally generated answers with citations.

## Current milestone

Version 0.1 focuses on the smallest useful pipeline:

1. Select a local folder.
2. Extract text from supported files.
3. Store file metadata and searchable content locally.
4. Search the indexed content and return matching sources.

## Project structure

```text
backend/       Python API and local search engine
frontend/      Desktop interface (added after the core engine works)
docs/          Architecture and product notes
sample_files/  Safe files for development and tests
```

## Local setup

From PowerShell in this directory:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
uvicorn backend.app.main:app --reload
```

Open `http://127.0.0.1:8000/health` to verify the API is running.

Run checks with:

```powershell
pytest
ruff check .
```

## Privacy principle

User documents, indexes, embeddings, and generated answers remain on the user's device by default. Networked features must be optional and explicit.

