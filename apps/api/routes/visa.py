"""Visa application routes."""

from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def visa_status() -> dict[str, str]:
    """Return placeholder visa info."""
    return {"result": "visa"}

