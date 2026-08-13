import pytest
from src.telemetry import measure_performance

def test_measure_performance_success():
    @measure_performance
    def sample_func(x: int, y: int) -> int:
        return x + y

    res = sample_func(5, 10)
    assert res == 15

def test_measure_performance_exception():
    @measure_performance
    def failing_func():
        raise ValueError("Error simulado")

    with pytest.raises(ValueError, match="Error simulado"):
        failing_func()