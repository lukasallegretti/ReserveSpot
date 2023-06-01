from fastapi.testclient import TestClient


def test_read_root(http_client: TestClient):
    hotel_name = "Hilton"
    response = http_client.get(f"/hotels/{hotel_name}")
    assert response.status_code == 200
    assert response.json() == {"hotel_name": "Hilton"}
