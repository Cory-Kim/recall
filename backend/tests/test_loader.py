from pathlib import Path

import pytest

from backend.app.ingestion import load_text_documents


def test_loads_text_documents_in_alphabetical_order(tmp_path: Path) -> None:
    (tmp_path / "zebra.txt").write_text("Second document", encoding="utf-8")
    (tmp_path / "alpha.txt").write_text("First document", encoding="utf-8")

    documents = load_text_documents(tmp_path)

    assert [document.filename for document in documents] == ["alpha.txt", "zebra.txt"]
    assert [document.content for document in documents] == ["First document", "Second document"]


def test_ignores_unsupported_files(tmp_path: Path) -> None:
    (tmp_path / "notes.txt").write_text("Included", encoding="utf-8")
    (tmp_path / "image.png").write_bytes(b"ignored")

    documents = load_text_documents(tmp_path)

    assert len(documents) == 1
    assert documents[0].filename == "notes.txt"


def test_empty_folder_returns_empty_list(tmp_path: Path) -> None:
    assert load_text_documents(tmp_path) == []


def test_missing_folder_raises_error(tmp_path: Path) -> None:
    missing_folder = tmp_path / "missing"

    with pytest.raises(FileNotFoundError, match="Folder does not exist"):
        load_text_documents(missing_folder)

