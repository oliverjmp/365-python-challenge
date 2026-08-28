import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from src.main import app
from src.tasks import heavy_computation

client = TestClient(app)

def test_heavy_computation_task_success():
    res = heavy_computation.run(duration=1, task_name="UnitTestTask")
    assert res["task_name"] == "UnitTestTask"
    assert res["status"] == "COMPLETED"

def test_heavy_computation_negative_duration():
    with pytest.raises(ValueError, match="La duración no puede ser negativa."):
        heavy_computation.run(duration=-1)

@patch("src.main.heavy_computation.delay")
def test_trigger_task_endpoint(mock_delay):
    mock_task = MagicMock()
    mock_task.id = "fake-uuid-1234"
    mock_delay.return_value = mock_task

    response = client.post("/tasks/trigger", json={"task_name": "TestReport", "duration": 2})
    assert response.status_code == 202
    data = response.json()
    assert data["task_id"] == "fake-uuid-1234"
    assert data["status"] == "PENDING"

@patch("src.main.heavy_computation.delay")
def test_trigger_task_endpoint_broker_exception(mock_delay):
    # Forzar excepción para cubrir el bloque except (fallback)
    mock_delay.side_effect = Exception("Redis connection refused")

    response = client.post("/tasks/trigger", json={"task_name": "TestReport", "duration": 2})
    assert response.status_code == 202
    data = response.json()
    assert data["task_id"] == "local-fallback-id"
    assert data["status"] == "SIMULATED"

@patch("src.main.AsyncResult")
def test_get_task_status_endpoint(mock_async_result):
    mock_res_instance = MagicMock()
    mock_res_instance.status = "SUCCESS"
    mock_res_instance.ready.return_value = True
    mock_res_instance.result = {"status": "COMPLETED"}
    mock_async_result.return_value = mock_res_instance

    response = client.get("/tasks/fake-uuid-1234")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "SUCCESS"

def test_get_task_status_fallback():
    response = client.get("/tasks/local-fallback-id")
    assert response.status_code == 200
    assert response.json()["status"] == "SUCCESS"