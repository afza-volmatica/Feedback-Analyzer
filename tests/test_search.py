from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():

    response = client.get(
        "/health"
    )

    assert response.status_code == 200

    assert response.json() == {
        "status": "healthy"
    }


def test_search():

    response = client.post(
        "/search",
        json={
            "query":
            "payment issue"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "results" in data

    assert len(
        data["results"]
    ) > 0