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


def test_scan_document(tmp_path: Path) -> None:
    path = tmp_path / "hello.txt"
    path.write_text("hello world")
    with path.open("rb") as f:
        resp = client.post("/documents/scan", files={"file": f})
    assert resp.status_code == 200
    assert "hello world" in resp.json()["text"]
