from fastapi.testclient import TestClient


def test_enpoint(http_client: TestClient):
    response = http_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
