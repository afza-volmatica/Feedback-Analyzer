from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_trends():

    response = client.get(
        "/trends"
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)

    if len(data) > 0:

        assert "month" in data[0]

        assert "topic" in data[0]

        assert "count" in data[0]