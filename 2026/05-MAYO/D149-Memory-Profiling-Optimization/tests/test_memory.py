import pytest
import pandas as pd
import numpy as np
from src.memory_profiler import MemoryProfilerEngine

def test_generate_heavy_dataframe_validation():
    """Valida la generación del DataFrame y control de errores por filas inválidas."""
    profiler = MemoryProfilerEngine()
    
    with pytest.raises(ValueError, match="debe ser mayor a cero"):
        profiler.generate_heavy_dataframe(num_rows=0)
        
    df = profiler.generate_heavy_dataframe(num_rows=100)
    assert not df.empty
    assert len(df) == 100

def test_get_memory_stats_empty_raises_error():
    """Valida que calcular estadísticas de un DataFrame vacío lance un ValueError."""
    profiler = MemoryProfilerEngine()
    with pytest.raises(ValueError, match="está vacío"):
        profiler.get_memory_stats(pd.DataFrame())

def test_optimize_dataframe_memory_empty_raises_error():
    """Valida que optimizar un DataFrame vacío lance un ValueError."""
    profiler = MemoryProfilerEngine()
    with pytest.raises(ValueError, match="está vacío"):
        profiler.optimize_dataframe_memory(pd.DataFrame())

def test_memory_optimization_reduces_footprint():
    """Valida que el proceso de optimización reduzca efectivamente el consumo de memoria."""
    profiler = MemoryProfilerEngine()
    df = profiler.generate_heavy_dataframe(num_rows=5_000)
    
    stats_before = profiler.get_memory_stats(df)
    optimized_df = profiler.optimize_dataframe_memory(df)
    stats_after = profiler.get_memory_stats(optimized_df)
    
    assert stats_after["bytes"] < stats_before["bytes"]
    assert optimized_df["categoria"].dtype.name == "category"

def test_measure_memory_usage_execution():
    """Valida el perfilamiento de memoria utilizando tracemalloc con una función externa."""
    profiler = MemoryProfilerEngine()
    
    def dummy_task():
        return pd.DataFrame({"a": range(10_000), "b": range(10_000)})

    result, peak_mb = profiler.measure_memory_usage(dummy_task)
    assert not result.empty
    assert peak_mb > 0.0