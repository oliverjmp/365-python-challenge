import pandas as pd
from src.profiler_engine import simulate_heavy_computation, profile_function

def test_simulate_heavy_computation():
    df = simulate_heavy_computation(delay=0.01)
    assert not df.empty
    assert len(df) == 1000
    assert "Valor" in df.columns

def test_profile_function():
    result, report = profile_function(simulate_heavy_computation, delay=0.01)
    assert not result.empty
    assert isinstance(report, str)
    assert "simulate_heavy_computation" in report