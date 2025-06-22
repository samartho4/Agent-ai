"""Background task placeholders for the worker service."""

from .ocr import process_ocr
from .embed import embed_document
from .zip import create_zip

__all__ = [
    "process_ocr",
    "embed_document",
    "create_zip",
]

