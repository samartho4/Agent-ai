from unittest.mock import AsyncMock, patch

from fastapi.testclient import TestClient

from apps.api.main import app


client = TestClient(app)


def test_generate_sop() -> None:
    with patch("agents.sop_generator.agent.generate", new_callable=AsyncMock) as mock_gen:
        mock_gen.return_value = "sample sop"
        resp = client.post("/sop/generate", json={"name": "Test"})

    assert resp.status_code == 200
    assert resp.json() == {"sop": "sample sop"}
