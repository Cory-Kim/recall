from pathlib import Path


def find_text_files(folder: Path) -> list[Path]:
    if not folder.exists():
        raise FileNotFoundError(f"Folder does not exist: {folder}")

    if not folder.is_dir():
        raise NotADirectoryError(f"Path is not a folder: {folder}")

    text_files = [
        path for path in folder.iterdir() if path.is_file() and path.suffix.lower() == ".txt"
    ]

    return sorted(text_files, key=lambda path: path.name.lower())

