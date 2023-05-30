from fastapi.testclient import TestClient
import pytest

from src.server import app


@pytest.fixture
def http_client() -> TestClient:
    return TestClient(app)
