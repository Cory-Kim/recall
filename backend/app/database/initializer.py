import sqlite3
from pathlib import Path

CREATE_DOCUMENTS_TABLE = """
CREATE TABLE IF NOT EXISTS documents (
    id INTEGER PRIMARY KEY,
    path TEXT NOT NULL UNIQUE,
    filename TEXT NOT NULL,
    content TEXT NOT NULL,
    size INTEGER NOT NULL
)
"""


def initialize_database(database_path: Path) -> None:
    database_path.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(database_path)

    try:
        connection.execute(CREATE_DOCUMENTS_TABLE)
        connection.commit()
    finally:
        connection.close()
