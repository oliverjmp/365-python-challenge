import pytest
from fastapi.testclient import TestClient
from src.main import app, limiter

client = TestClient(app)

@pytest.fixture(autouse=True)
def reset_rate_limit():
    """Reinicia el almacenamiento del limitador antes de cada prueba para evitar interferencias."""
    limiter.reset()
    yield

def test_rate_limit_allowed():
    """Valida que las peticiones dentro del límite sean permitidas."""
    response = client.get("/analytics/data")
    assert response.status_code == 200
    assert response.json()["status"] == "success"

def test_rate_limit_exceeded():
    """Valida que se bloqueen las peticiones al exceder el límite establecido (5 por minuto)."""
    for _ in range(5):
        res = client.get("/analytics/data")
        assert res.status_code == 200

    response = client.get("/analytics/data")
    assert response.status_code == 429