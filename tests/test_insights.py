from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_insights():

    response = client.get(
        "/insights"
    )

    assert response.status_code == 200

    data = response.json()

    assert "total_reviews" in data

    assert "top_complaint" in data

    assert "complaint_count" in data