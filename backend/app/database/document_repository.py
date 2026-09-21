import sqlite3
from pathlib import Path

from backend.app.ingestion.models import Document

INSERT_DOCUMENT = """
INSERT INTO documents (path, filename, content, size)
VALUES (?, ?, ?, ?)
"""


def save_document(database_path: Path, document: Document) -> int:
    connection = sqlite3.connect(database_path)

    try:
        cursor = connection.execute(
            INSERT_DOCUMENT,
            (str(document.path), document.filename, document.content, document.size),
        )
        connection.commit()

        if cursor.lastrowid is None:
            raise RuntimeError("SQLite did not return an id for the saved document")

        return cursor.lastrowid
    finally:
        connection.close()

