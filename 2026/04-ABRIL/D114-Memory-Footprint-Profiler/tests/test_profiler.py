import pytest
from src.profiler import MemoryProfiler

def sample_heavy_task(n: int) -> list:
    """Función de prueba que genera una cantidad grande de datos en memoria."""
    return [i * i for i in range(n)]

def test_measure_memory_usage_success():
    result, metrics = MemoryProfiler.measure_memory_usage(sample_heavy_task, 100000)
    
    assert len(result) == 100000
    assert "current_memory_kb" in metrics
    assert "peak_memory_kb" in metrics
    assert "execution_time_sec" in metrics
    assert metrics["peak_memory_kb"] > 0
    assert metrics["execution_time_sec"] >= 0

def test_profiler_structure():
    assert hasattr(MemoryProfiler, "measure_memory_usage")
    assert isinstance(MemoryProfiler.moverse_a_generadores, str)