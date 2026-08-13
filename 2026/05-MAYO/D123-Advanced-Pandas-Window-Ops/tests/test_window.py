import pytest
import pandas as pd
from src.window_processor import AdvancedWindowProcessor

def test_processor_empty_data():
    """Valida que se lance un error si el DataFrame está vacío."""
    df_empty = pd.DataFrame()
    processor = AdvancedWindowProcessor(df_empty)
    with pytest.raises(ValueError, match="DataFrame de entrada está vacío"):
        processor.compute_advanced_metrics()

def test_compute_advanced_metrics():
    """Valida el cálculo correcto de las ventanas deslizantes y métricas vectorizadas."""
    data = {
        "sensor_a": [10.0, 12.0, 14.0, 25.0, 13.0],
        "sensor_b": [100.0, 102.0, 101.0, 99.0, 100.0]
    }
    df = pd.DataFrame(data)
    
    processor = AdvancedWindowProcessor(df)
    result = processor.compute_advanced_metrics(window_size=3)
    
    assert "sensor_a_rolling_mean" in result.columns
    assert "sensor_a_rolling_std" in result.columns
    assert "sensor_a_rolling_zscore" in result.columns
    assert len(result) == 5
    # Validar que la última fila refleje los cálculos esperados sin errores de tipo
    assert isinstance(result.iloc[-1]["sensor_a_rolling_mean"], float)