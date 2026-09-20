"""Document discovery and text extraction."""

from backend.app.ingestion.models import Document
from backend.app.ingestion.text_reader import read_text_file

__all__ = ["Document", "read_text_file"]

