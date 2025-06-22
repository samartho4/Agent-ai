"""Statement of Purpose generation routes."""

from fastapi import APIRouter, Body

from agents.sop_generator import agent

router = APIRouter()


@router.post("/generate")
async def generate_sop(profile: dict = Body(...)) -> dict[str, str]:
    """Return an SOP draft for the given profile."""
    text = await agent.generate(profile)
    return {"sop": text}

