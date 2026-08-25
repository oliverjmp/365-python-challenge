import pytest
from src.benchmark_runner import BenchmarkRunner

def test_benchmark_inicializacion():
    """Verifica que el motor de benchmark inicialice correctamente con el dataset."""
    runner = BenchmarkRunner(num_filas=1000)
    assert runner.df is not None
    assert runner.conn is not None

def test_ejecucion_comparativa():
    """Valida que los benchmarks retornen métricas válidas de tiempo y mejora."""
    runner = BenchmarkRunner(num_filas=1000)
    resultado = runner.ejecutar_comparativa()
    
    assert "pandas_segundos" in resultado
    assert "duckdb_segundos" in resultado
    assert resultado["filas"] == 1000
    assert isinstance(resultado["mejora_x"], float)