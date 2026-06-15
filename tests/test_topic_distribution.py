from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_topic_distribution():

    response = client.get(
        "/topic-distribution"
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, dict)

    assert len(data) > 0