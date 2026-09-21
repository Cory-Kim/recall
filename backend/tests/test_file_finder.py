from pathlib import Path

import pytest

from backend.app.ingestion import find_text_files


def test_finds_text_files_in_alphabetical_order(tmp_path: Path) -> None:
    later_file = tmp_path / "zebra.txt"
    earlier_file = tmp_path / "alpha.TXT"
    later_file.write_text("Later", encoding="utf-8")
    earlier_file.write_text("Earlier", encoding="utf-8")

    files = find_text_files(tmp_path)

    assert files == [earlier_file, later_file]


def test_ignores_unsupported_files(tmp_path: Path) -> None:
    text_file = tmp_path / "notes.txt"
    text_file.write_text("Included", encoding="utf-8")
    (tmp_path / "image.png").write_bytes(b"ignored")

    assert find_text_files(tmp_path) == [text_file]


def test_does_not_scan_subfolders(tmp_path: Path) -> None:
    nested_folder = tmp_path / "nested"
    nested_folder.mkdir()
    (nested_folder / "hidden.txt").write_text("Not included yet", encoding="utf-8")

    assert find_text_files(tmp_path) == []


def test_empty_folder_returns_empty_list(tmp_path: Path) -> None:
    assert find_text_files(tmp_path) == []


def test_missing_folder_raises_error(tmp_path: Path) -> None:
    missing_folder = tmp_path / "missing"

    with pytest.raises(FileNotFoundError, match="Folder does not exist"):
        find_text_files(missing_folder)


def test_file_path_raises_error(tmp_path: Path) -> None:
    file_path = tmp_path / "notes.txt"
    file_path.write_text("Not a folder", encoding="utf-8")

    with pytest.raises(NotADirectoryError, match="Path is not a folder"):
        find_text_files(file_path)

