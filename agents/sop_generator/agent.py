"""Generate Statements of Purpose via Gemini."""

from typing import Any

from libs.llm import GeminiClient


async def generate(profile: dict[str, Any]) -> str:
    """Return a short SOP draft for the given student profile."""
    client = GeminiClient()
    return await client.generate_sop(profile)
