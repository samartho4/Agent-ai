"""Tests for the document upload endpoint."""

from pathlib import Path

from fastapi.testclient import TestClient

from apps.api.main import app


client = TestClient(app)


def test_upload_document(tmp_path: Path) -> None:
    upload_path = tmp_path / "sample.txt"
    upload_path.write_text("example")

    with upload_path.open("rb") as f:
        response = client.post("/documents/upload", files={"file": f})

    assert response.status_code == 200
    assert response.json()["filename"] == "sample.txt"
