"""College lookup routes."""

from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def list_colleges() -> dict[str, str]:
    """Return placeholder college list."""
    return {"result": "colleges"}

