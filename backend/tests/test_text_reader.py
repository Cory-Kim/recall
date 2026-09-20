from pathlib import Path

import pytest

from backend.app.ingestion import Document, read_text_file


def test_read_text_file(tmp_path: Path) -> None:
    file_path = tmp_path / "notes.txt"
    file_path.write_text("Local search keeps files private.", encoding="utf-8")

    document = read_text_file(file_path)

    assert document == Document(
        path=file_path,
        filename="notes.txt",
        content="Local search keeps files private.",
        size=file_path.stat().st_size,
    )


def test_read_empty_text_file(tmp_path: Path) -> None:
    file_path = tmp_path / "empty.txt"
    file_path.write_text("", encoding="utf-8")

    document = read_text_file(file_path)

    assert document.content == ""
    assert document.size == 0


def test_rejects_unsupported_file_type(tmp_path: Path) -> None:
    file_path = tmp_path / "notes.pdf"
    file_path.write_bytes(b"not a real PDF")

    with pytest.raises(ValueError, match="Unsupported file type: .pdf"):
        read_text_file(file_path)


def test_missing_text_file_raises_error(tmp_path: Path) -> None:
    missing_path = tmp_path / "missing.txt"

    with pytest.raises(FileNotFoundError):
        read_text_file(missing_path)

