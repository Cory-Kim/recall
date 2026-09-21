"""Local persistence layer."""

from backend.app.database.document_repository import save_document
from backend.app.database.initializer import initialize_database

__all__ = ["initialize_database", "save_document"]

