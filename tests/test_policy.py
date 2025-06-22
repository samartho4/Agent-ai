from unittest.mock import AsyncMock, patch

from apps.api.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


async def fake_get(*args, **kwargs):
    class Resp:
        def raise_for_status(self):
            pass

        def json(self):
            return [{"title": "Test", "date": "2025-01-01", "url": "u"}]

    return Resp()


def test_latest_policy() -> None:
    with patch("httpx.AsyncClient.get", new=AsyncMock(side_effect=fake_get)):
        resp = client.get("/policy/latest")

    assert resp.status_code == 200
    assert resp.json()["news"][0]["title"] == "Test"
