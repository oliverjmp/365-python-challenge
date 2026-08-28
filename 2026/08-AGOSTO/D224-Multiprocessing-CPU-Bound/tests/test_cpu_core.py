import pytest
from src.cpu_core import compute_heavy_math, MultiprocessingCPUBoundManager

def test_compute_heavy_math_success():
    res = compute_heavy_math(5)
    assert res == 120

def test_compute_heavy_math_negative():
    with pytest.raises(ValueError, match="El número no puede ser negativo."):
        compute_heavy_math(-1)

def test_compute_batch_success():
    manager = MultiprocessingCPUBoundManager()
    summary = manager.compute_batch([10, 20, 30], max_workers=2)
    assert summary["total_computations"] == 3
    assert len(summary["results"]) == 3
    assert summary["results"][0]["status"] == "SUCCESS"

def test_compute_batch_exception_branch():
    manager = MultiprocessingCPUBoundManager()
    # Introducir un número negativo en el lote forzará la excepción que cubre las líneas 29-30
    summary = manager.compute_batch([-5], max_workers=1)
    assert summary["total_computations"] == 1
    assert summary["results"][0]["status"] == "FAILED"
    assert "error" in summary["results"][0]

def test_compute_batch_empty_list():
    manager = MultiprocessingCPUBoundManager()
    with pytest.raises(ValueError, match="La lista de números no puede estar vacía."):
        manager.compute_batch([])

def test_compute_batch_invalid_workers():
    manager = MultiprocessingCPUBoundManager()
    with pytest.raises(ValueError, match="El número de workers debe ser mayor a cero."):
        manager.compute_batch([10, 20], max_workers=0)