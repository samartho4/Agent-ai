"""Helpers for saving uploaded documents."""

from pathlib import Path

from fastapi import UploadFile


async def save_file(file: UploadFile, dest_dir: Path) -> Path:
    """Persist an uploaded file to ``dest_dir`` and return the path."""
    dest_dir.mkdir(parents=True, exist_ok=True)
    file_path = dest_dir / file.filename
    with file_path.open("wb") as f:
        f.write(await file.read())
    return file_path

