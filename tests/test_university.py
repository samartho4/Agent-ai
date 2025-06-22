from unittest.mock import patch

from fastapi.testclient import TestClient

from apps.api.main import app

client = TestClient(app)


def test_match_program() -> None:
    sample = [
        {"institution": "X", "program": "Data Science", "level": "Masters", "province": "ON"}
    ]
    with patch("services.university.matcher.load_programs", return_value=sample):
        resp = client.post("/university/match", json={"program": "Data Science"})

    assert resp.status_code == 200
    assert resp.json()["matches"][0]["program"] == "Data Science"
