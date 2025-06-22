"""University matcher routes."""

from fastapi import APIRouter, Body

from services.university import find_matches

router = APIRouter()


@router.post("/match")
async def match_program(profile: dict = Body(...)) -> dict[str, list[dict]]:
    """Return best program matches for the given profile."""
    results = find_matches(profile)
    return {"matches": results}
