"""Authentication related routes."""

from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def auth_root() -> dict[str, str]:
    """Placeholder endpoint for auth."""
    return {"status": "auth"}

