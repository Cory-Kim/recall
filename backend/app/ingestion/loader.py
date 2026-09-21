from pathlib import Path

from backend.app.ingestion.file_finder import find_text_files
from backend.app.ingestion.models import Document
from backend.app.ingestion.text_reader import read_text_file


def load_text_documents(folder: Path) -> list[Document]:
    files = find_text_files(folder)
    documents = []

    for file_path in files:
        document = read_text_file(file_path)
        documents.append(document)

    return documents

