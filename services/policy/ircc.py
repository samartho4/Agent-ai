"""IRCC policy fetcher."""

from __future__ import annotations

import httpx
from typing import Any, List

IRCC_NEWS_URL = "https://www.canada.ca/content/dam/ircc/documents/json/ircc-news.json"


async def fetch_latest_news() -> List[dict[str, Any]]:
    """Fetch the latest IRCC news items.

    If the HTTP request fails, a static fallback item is returned.
    """
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(IRCC_NEWS_URL, timeout=10)
            resp.raise_for_status()
            data = resp.json()
            if isinstance(data, list):
                return data
    except Exception:
        pass
    return [
        {
            "title": "IRCC announces updated student visa guidelines",
            "date": "2024-12-01",
            "url": "https://www.canada.ca/en/immigration-refugees-citizenship/news/2024/12/update.html",
        }
    ]
