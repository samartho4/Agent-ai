"""Notification routes."""

from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def notify_placeholder() -> dict[str, str]:
    """Return placeholder notification response."""
    return {"result": "notify"}

