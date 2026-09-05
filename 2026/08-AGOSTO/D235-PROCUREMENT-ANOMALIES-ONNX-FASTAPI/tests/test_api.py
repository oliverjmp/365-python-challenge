import pytest
import importlib
from fastapi.testclient import TestClient
import src.api as api_module
from src.api import app

client = TestClient(app)

def test_health_check_success():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "operational"

def test_detect_anomaly_success():
    payload = {
        "monto": 15000.50,
        "frecuencia_proveedor": 1.2,
        "desviacion_precio": 0.45
    }
    response = client.post("/detect", json=payload)
    assert response.status_code == 200
    assert "anomaly_detected" in response.json()
    assert isinstance(response.json()["anomaly_detected"], bool)

def test_detect_anomaly_validation_error():
    payload = {
        "monto": -100, 
        "frecuencia_proveedor": 1.2,
        "desviacion_precio": 0.45
    }
    response = client.post("/detect", json=payload)
    assert response.status_code == 422

def test_model_not_loaded_errors(monkeypatch):
    monkeypatch.setattr(api_module, "session", None)
    
    response_health = client.get("/health")
    assert response_health.status_code == 500
    
    response_detect = client.post("/detect", json={"monto": 100, "frecuencia_proveedor": 1, "desviacion_precio": 0})
    assert response_detect.status_code == 500

def test_model_load_exception(monkeypatch):
    """Cubre el bloque except de la inicialización del modelo (Líneas 17-18)."""
    import onnxruntime as rt
    
    # Forzamos que el motor ONNX falle al intentar cargar cualquier archivo
    def mock_init_error(*args, **kwargs):
        raise Exception("Fallo de inicialización simulado para cobertura")
        
    monkeypatch.setattr(rt, "InferenceSession", mock_init_error)
    
    # Al recargar el módulo, usará el mock y caerá obligatoriamente en el except
    importlib.reload(api_module)
    assert api_module.session is None
    
    # Deshacemos el parche y recargamos nuevamente para no afectar al resto de pruebas
    monkeypatch.undo()
    importlib.reload(api_module)

def test_detect_anomaly_inference_error(monkeypatch):
    """Cubre el bloque except de error durante la inferencia ONNX (Líneas 44-45)."""
    importlib.reload(api_module)
    
    class MockSession:
        def run(self, *args, **kwargs):
            raise RuntimeError("Fallo de hardware simulado en ONNX")
            
    monkeypatch.setattr(api_module, "session", MockSession())
    
    local_client = TestClient(api_module.app)
    
    payload = {
        "monto": 15000.50,
        "frecuencia_proveedor": 1.2,
        "desviacion_precio": 0.45
    }
    response = local_client.post("/detect", json=payload)
    
    assert response.status_code == 400
    assert "Fallo de hardware simulado" in response.json()["detail"]