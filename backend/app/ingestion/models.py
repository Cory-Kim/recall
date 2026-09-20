from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class Document:
    path: Path
    filename: str
    content: str
    size: int

