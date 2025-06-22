from __future__ import annotations

"""Document OCR and parsing helpers."""

from pathlib import Path
from typing import Any

from pdfminer.high_level import extract_text


def extract_document_text(path: Path) -> str:
    """Return extracted text from a PDF or text file."""
    try:
        return extract_text(path)
    except Exception:
        try:
            return path.read_text()
        except Exception:
            return ""
