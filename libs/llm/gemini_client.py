import os
from typing import Any

import httpx


class GeminiClient:
    """Thin wrapper for the Gemini generative API."""

    def __init__(self, api_key: str | None = None) -> None:
        self.api_key = api_key or os.getenv("GEMINI_API_KEY", "")
        self.endpoint = (
            "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
        )

    async def generate_sop(self, profile: dict[str, Any]) -> str:
        """Generate a short Statement of Purpose for the given profile."""
        prompt = (
            "Write a concise Canadian study visa Statement of Purpose for the following profile: "
            f"{profile}"
        )
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        async with httpx.AsyncClient() as client:
            resp = await client.post(
                self.endpoint,
                params={"key": self.api_key},
                json=payload,
                timeout=30,
            )
            resp.raise_for_status()
            data = resp.json()
            return (
                data.get("candidates", [{}])[0]
                .get("content", {})
                .get("parts", [{}])[0]
                .get("text", "")
            )
