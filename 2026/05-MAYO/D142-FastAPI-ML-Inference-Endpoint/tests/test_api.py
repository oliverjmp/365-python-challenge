import pytest
from fastapi.testclient import TestClient
from src.main import app, inference_service
import src.main as main_module

client = TestClient(app)

def test_health_check():
    """Prueba el endpoint de salud de la API."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_predict_endpoint_success():
    """Prueba el endpoint de predicción POST con datos válidos."""
    response = client.post("/predict", json={"features": [1.0, -0.5, 2.1, 0.0]})
    assert response.status_code == 200
    data = response.json()
    assert "prediction" in data
    assert "probability" in data

def test_predict_endpoint_bad_request():
    """Prueba el manejo de errores al enviar un payload con datos vacíos."""
    response = client.post("/predict", json={"features": []})
    assert response.status_code == 400

def test_health_check_service_none(monkeypatch):
    """Prueba el error 500 cuando el servicio de inferencia no está disponible."""
    monkeypatch.setattr(main_module, "inference_service", None)
    response = client.get("/health")
    assert response.status_code == 500

def test_predict_service_none(monkeypatch):
    """Prueba el error 500 en /predict cuando el servicio es None."""
    monkeypatch.setattr(main_module, "inference_service", None)
    response = client.post("/predict", json={"features": [1.0, 2.0]})
    assert response.status_code == 500

def test_predict_internal_exception(monkeypatch):
    """Prueba el manejo de errores internos genéricos durante la inferencia."""
    class MockErrorService:
        def predict(self, features):
            raise RuntimeError("Error inesperado de prueba")
    
    monkeypatch.setattr(main_module, "inference_service", MockErrorService())
    response = client.post("/predict", json={"features": [1.0, 2.0]})
    assert response.status_code == 500

def test_model_load_exception(monkeypatch):
    """Cubre el bloque try-except de inicialización de inference_service en main.py (Líneas 15-16)."""
    import importlib
    import src.main as main_mod
    import src.model_service as svc_mod

    # Forzamos un error al instanciar el servicio para cubrir la excepción del bloque principal
    def mock_init_error(*args, **kwargs):
        raise Exception("Error simulado de carga de modelo")

    monkeypatch.setattr(svc_mod, "ModelInferenceService", mock_init_error)
    
    # Recargamos el módulo para disparar el try-except con la excepción simulada
    importlib.reload(main_mod)
    
    # Restauramos el módulo para no afectar otras pruebas
    monkeypatch.undo()
    importlib.reload(main_mod)