from fastapi.testclient import TestClient


def test_read_root(http_client: TestClient):
    response = http_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_read_item(http_client: TestClient):
    response = http_client.get("/items/25")
    assert response.status_code == 200
    assert response.json() == {"item_id": 25}


def test_pass_wrong_typing_to_item_id(http_client: TestClient):
    response = http_client.get("/items/foo")
    assert response.status_code == 422
