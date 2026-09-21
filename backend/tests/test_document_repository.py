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


def test_updates_document_when_path_already_exists(tmp_path: Path) -> None:
    database_path = tmp_path / "recall.db"
    initialize_database(database_path)
    original_document = Document(Path("notes.txt"), "notes.txt", "Original", 8)
    edited_document = Document(Path("notes.txt"), "notes.txt", "Edited content", 14)

    original_id = save_document(database_path, original_document)
    updated_id = save_document(database_path, edited_document)

    with sqlite3.connect(database_path) as connection:
        saved_rows = connection.execute(
            "SELECT id, path, filename, content, size FROM documents"
        ).fetchall()

    assert updated_id == original_id
    assert saved_rows == [
        (
            original_id,
            str(edited_document.path),
            edited_document.filename,
            edited_document.content,
            edited_document.size,
        )
    ]
