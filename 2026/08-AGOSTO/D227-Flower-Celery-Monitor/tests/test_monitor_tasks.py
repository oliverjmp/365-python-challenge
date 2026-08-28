import pytest
from unittest.mock import patch
from src.monitor_tasks import monitored_computation

def test_monitored_computation_success():
    # Prueba síncrona donde self.request.id es None
    result = monitored_computation.run(items_count=2, task_tag="UnitTest")
    
    assert result["task_tag"] == "UnitTest"
    assert result["items_processed"] == 2
    assert result["status"] == "SUCCESS"

def test_monitored_computation_with_request_id():
    # Simulamos el backend para evitar la conexión real a Redis cuando se llama update_state
    monitored_computation.request.id = "mock-task-id-12345"
    with patch.object(monitored_computation, "update_state") as mock_update:
        try:
            result = monitored_computation.run(items_count=1, task_tag="MockIDTest")
            assert result["task_id"] == "mock-task-id-12345"
            assert result["status"] == "SUCCESS"
            assert mock_update.called
        finally:
            monitored_computation.request.id = None

def test_monitored_computation_negative_items():
    with pytest.raises(ValueError, match="El conteo de elementos no puede ser negativo."):
        monitored_computation.run(items_count=-1)