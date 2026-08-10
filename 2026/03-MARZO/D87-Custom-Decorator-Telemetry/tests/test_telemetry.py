import pytest
from src.telemetry import monitor_telemetry

def test_successful_telemetry_execution():
    """Valida que una función decorada se ejecute correctamente y conserve su valor de retorno."""
    @monitor_telemetry
    def sample_addition(a: int, b: int) -> int:
        return a + b

    result = sample_addition(5, 10)
    assert result == 15
    assert sample_addition.__name__ == "sample_addition"

def test_failed_telemetry_execution():
    """Valida que el decorador capture y propague excepciones manteniendo la telemetría."""
    @monitor_telemetry
    def faulty_function():
        raise ValueError("Error crítico simulado")

    with pytest.raises(ValueError, match="Error crítico simulado"):
        faulty_function()