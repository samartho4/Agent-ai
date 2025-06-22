"""Document management routes."""

from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def list_documents() -> dict[str, str]:
    """Return placeholder document list."""
    return {"result": "documents"}

