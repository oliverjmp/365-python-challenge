import pytest
from unittest.mock import MagicMock
from src.search_client import LogSearchClient

@pytest.fixture
def mock_es_client():
    client = MagicMock()
    return client

def test_create_index(mock_es_client):
    """Valida la creación del índice cuando no existe."""
    mock_es_client.indices.exists.return_value = False
    mock_es_client.indices.create.return_value = {"acknowledged": True}

    client = LogSearchClient(mock_es_client, index_name="test-logs")
    response = client.create_index()

    assert response["acknowledged"] is True
    mock_es_client.indices.create.assert_called_once_with(index="test-logs")

def test_index_log(mock_es_client):
    """Valida la indexación de un registro de log."""
    mock_es_client.index.return_value = {"result": "created"}

    client = LogSearchClient(mock_es_client, index_name="test-logs")
    log_data = {"level": "INFO", "message": "Database connection established successfully"}
    response = client.index_log("1", log_data)

    assert response["result"] == "created"
    mock_es_client.index.assert_called_once()

def test_search_logs(mock_es_client):
    """Valida la búsqueda de texto completo sobre los logs."""
    mock_es_client.search.return_value = {
        "hits": {
            "hits": [
                {"_source": {"level": "ERROR", "message": "Connection timeout error"}}
            ]
        }
    }

    client = LogSearchClient(mock_es_client, index_name="test-logs")
    results = client.search_logs("timeout")

    assert len(results) == 1
    assert results[0]["level"] == "ERROR"
    assert "timeout" in results[0]["message"]

def test_create_index_already_exists(mock_es_client):
    """Valida el comportamiento cuando el índice ya existe en Elasticsearch."""
    # Simulamos que el índice SÍ existe
    mock_es_client.indices.exists.return_value = True

    client = LogSearchClient(mock_es_client, index_name="test-logs")
    response = client.create_index()

    # Verificamos que devuelva el mensaje de que ya existe
    assert response["acknowledged"] is False
    assert response["message"] == "Index already exists"
    mock_es_client.indices.create.assert_not_called()