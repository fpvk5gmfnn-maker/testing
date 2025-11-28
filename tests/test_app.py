from fastapi.testclient import TestClient

from app.main import app
from app.summary import generate_summary

client = TestClient(app)


def test_generate_summary_multi_sentence():
    text = "FastAPI makes it easy to build APIs quickly. It uses type hints to validate requests. The developer experience is excellent."
    summary = generate_summary(text)
    assert "FastAPI makes it easy" in summary
    assert len(summary) < len(text)


def test_create_summary_endpoint():
    payload = {"text": "Testing the summary endpoint with FastAPI."}
    response = client.post("/summaries", json=payload)
    assert response.status_code == 200
    body = response.json()
    assert "summary" in body
    assert body["original_length"] == len(payload["text"])


def test_homepage_serves_html():
    response = client.get("/")
    assert response.status_code == 200
    assert "Summarize text with a clean FastAPI demo" in response.text
