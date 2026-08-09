from fastapi.testclient import TestClient
from src.main import app

# Inicializamos el cliente indicando que no eleve las excepciones del servidor
client = TestClient(app, raise_server_exceptions=False)

def test_success_resource():
    """Valida que una petición correcta devuelva el recurso con éxito."""
    response = client.get("/analytics/resource/ventas")
    assert response.status_code == 200
    assert response.json()["status"] == "success"

def test_business_exception_handler():
    """Valida la captura y estandarización de la excepción de negocio (404)."""
    response = client.get("/analytics/resource/unknown")
    assert response.status_code == 404
    data = response.json()
    assert data["status"] == "error"
    assert "no fue encontrado" in data["message"]

def test_global_exception_handler():
    """Valida la captura de errores genéricos no controlados del servidor (500)."""
    # Forzamos la desactivación temporal del middleware de errores de Starlette para el test
    app.middleware_stack = app.build_middleware_stack()
    response = client.get("/analytics/error")
    assert response.status_code == 500
    data = response.json()
    assert data["status"] == "error"
    assert data["message"] == "Ocurrió un error interno en el servidor."