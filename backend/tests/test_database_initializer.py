import sqlite3
from pathlib import Path

from backend.app.database import initialize_database


def test_creates_database_file_and_parent_folder(tmp_path: Path) -> None:
    database_path = tmp_path / "data" / "recall.db"

    initialize_database(database_path)

    assert database_path.is_file()


def test_creates_documents_table_with_expected_columns(tmp_path: Path) -> None:
    database_path = tmp_path / "recall.db"
    initialize_database(database_path)

    with sqlite3.connect(database_path) as connection:
        columns = connection.execute("PRAGMA table_info(documents)").fetchall()

    column_names = [column[1] for column in columns]
    assert column_names == ["id", "path", "filename", "content", "size"]


def test_initialization_can_run_more_than_once(tmp_path: Path) -> None:
    database_path = tmp_path / "recall.db"

    initialize_database(database_path)
    initialize_database(database_path)

    with sqlite3.connect(database_path) as connection:
        table_count = connection.execute(
            "SELECT COUNT(*) FROM sqlite_master WHERE type = 'table' AND name = 'documents'"
        ).fetchone()[0]

    assert table_count == 1

