import pytest
from fastapi.testclient import TestClient
from main import app
from src.analytics_service import AnalyticsService

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "activo"

def test_analytics_service_logic():
    service = AnalyticsService()
    resumen = service.obtener_resumen()
    assert isinstance(resumen, list)
    assert len(resumen) > 0

def test_analytics_endpoint():
    response = client.get("/analytics/summary")
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["status"] == "success"
    assert "data" in json_data