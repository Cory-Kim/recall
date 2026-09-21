import sqlite3
from pathlib import Path

from backend.app.database import initialize_database, save_document
from backend.app.ingestion import Document


def test_saves_document_and_returns_its_id(tmp_path: Path) -> None:
    database_path = tmp_path / "recall.db"
    initialize_database(database_path)
    document = Document(
        path=Path("notes/example.txt"),
        filename="example.txt",
        content="RECALL keeps this text searchable.",
        size=32,
    )

    document_id = save_document(database_path, document)

    with sqlite3.connect(database_path) as connection:
        saved_row = connection.execute(
            "SELECT id, path, filename, content, size FROM documents"
        ).fetchone()

    assert saved_row == (
        document_id,
        str(document.path),
        document.filename,
        document.content,
        document.size,
    )


def test_saved_documents_receive_different_ids(tmp_path: Path) -> None:
    database_path = tmp_path / "recall.db"
    initialize_database(database_path)
    first_document = Document(Path("first.txt"), "first.txt", "First", 5)
    second_document = Document(Path("second.txt"), "second.txt", "Second", 6)

    first_id = save_document(database_path, first_document)
    second_id = save_document(database_path, second_document)

    assert first_id != second_id

