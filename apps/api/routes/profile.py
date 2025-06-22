"""User profile routes."""

from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def get_profile() -> dict[str, str]:
    """Return placeholder profile."""
    return {"result": "profile"}

