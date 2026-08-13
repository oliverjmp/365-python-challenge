import pytest
from src.external_service import ExternalAPIClient

@pytest.fixture
def api_client():
    """Fixture que provee una instancia configurada del cliente de API."""
    return ExternalAPIClient(base_url="https://api.thirdpartyservice.com", api_key="mock_secret_key_123")

class MockResponse:
    def __init__(self, json_data, status_code):
        self._json_data = json_data
        self.status_code = status_code

    def json(self):
        return self._json_data

def test_get_user_success(api_client, monkeypatch):
    """Prueba exitosa simulando la respuesta de la API externa (Mocking)."""
    def mock_get(url, headers):
        assert "Authorization" in headers
        assert headers["Authorization"] == "Bearer mock_secret_key_123"
        return MockResponse({"id": 42, "name": "Oliver Profesional", "status": "active"}, 200)

    monkeypatch.setattr("requests.get", mock_get)

    data = api_client.get_user_data(42)
    assert data["id"] == 42
    assert data["name"] == "Oliver Profesional"

def test_get_user_not_found(api_client, monkeypatch):
    """Prueba de manejo de error 404 del servicio externo."""
    def mock_get(url, headers):
        return MockResponse({"error": "Not Found"}, 404)

    monkeypatch.setattr("requests.get", mock_get)

    with pytest.raises(ValueError, match="no encontrado"):
        api_client.get_user_data(999)

def test_get_user_server_error(api_client, monkeypatch):
    """Prueba de manejo de error crítico de servidor (500)."""
    def mock_get(url, headers):
        return MockResponse({"error": "Internal Error"}, 500)

    monkeypatch.setattr("requests.get", mock_get)

    with pytest.raises(ConnectionError, match="Código HTTP 500"):
        api_client.get_user_data(1)