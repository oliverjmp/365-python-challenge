from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_root():
    """Valida la respuesta del endpoint raíz."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_health_check():
    """Valida la respuesta del endpoint de salud."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"