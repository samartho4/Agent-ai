"""IRCC policy update routes."""

from fastapi import APIRouter

from services.policy import fetch_latest_news

router = APIRouter()


@router.get("/latest")
async def latest_policy() -> dict[str, list[dict[str, str]]]:
    """Return latest IRCC policy news."""
    news = await fetch_latest_news()
    return {"news": news}
