"""Document discovery and text extraction."""

from backend.app.ingestion.file_finder import find_text_files
from backend.app.ingestion.models import Document
from backend.app.ingestion.text_reader import read_text_file

__all__ = ["Document", "find_text_files", "read_text_file"]

