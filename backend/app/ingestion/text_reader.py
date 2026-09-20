from pathlib import Path

from backend.app.ingestion.models import Document


def read_text_file(path: Path) -> Document:
    if path.suffix.lower() != ".txt":
        raise ValueError(f"Unsupported file type: {path.suffix or 'no extension'}")

    content = path.read_text(encoding="utf-8")

    return Document(
        path=path,
        filename=path.name,
        content=content,
        size=path.stat().st_size,
    )

