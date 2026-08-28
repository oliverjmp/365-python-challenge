import pytest
from src.tasks import heavy_background_computation

def test_heavy_background_computation_success():
    # Prueba directa síncrona de la función subyacente de la tarea para asegurar cobertura 100%
    result = heavy_background_computation.run(duration=0.01, task_name="TestUnitTask")
    
    assert result["task_name"] == "TestUnitTask"
    assert result["duration_seconds"] == 0.01
    assert result["status"] == "COMPLETED"

def test_heavy_background_computation_negative_duration():
    with pytest.raises(ValueError, match="La duración de la tarea no puede ser negativa."):
        heavy_background_computation.run(duration=-1)