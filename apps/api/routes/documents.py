"""Document management routes."""

from pathlib import Path

from fastapi import APIRouter, File, UploadFile

from services.documents import save_file


router = APIRouter()


@router.get("/")
async def list_documents() -> dict[str, str]:
    """Return placeholder document list."""
    return {"result": "documents"}


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)) -> dict[str, str]:
    """Accept a document upload and store it locally."""
    uploads_dir = Path("uploads")
    await save_file(file, uploads_dir)
    return {"filename": file.filename}

