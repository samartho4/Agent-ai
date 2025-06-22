"""Statement of Purpose generation routes."""

from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def generate_sop() -> dict[str, str]:
    """Return placeholder SOP."""
    return {"result": "sop"}

