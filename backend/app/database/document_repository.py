import sqlite3
from pathlib import Path

from backend.app.ingestion.models import Document

UPSERT_DOCUMENT = """
INSERT INTO documents (path, filename, content, size)
VALUES (?, ?, ?, ?)
ON CONFLICT(path) DO UPDATE SET
    filename = excluded.filename,
    content = excluded.content,
    size = excluded.size
RETURNING id
"""


def save_document(database_path: Path, document: Document) -> int:
    connection = sqlite3.connect(database_path)

    try:
        cursor = connection.execute(
            UPSERT_DOCUMENT,
            (str(document.path), document.filename, document.content, document.size),
        )
        saved_row = cursor.fetchone()
        connection.commit()

        if saved_row is None:
            raise RuntimeError("SQLite did not return an id for the saved document")

        return saved_row[0]
    finally:
        connection.close()
