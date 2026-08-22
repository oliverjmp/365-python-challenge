import pytest
import numpy as np
from src.drift_detector import DataDriftDetector

def test_invalid_significance_level_raises_error():
    """Valida que un nivel de significancia fuera de rango lance un ValueError."""
    with pytest.raises(ValueError, match="debe estar entre 0.0 y 1.0"):
        DataDriftDetector(significance_level=1.5)

def test_null_data_raises_error():
    """Valida que pasar datos nulos lance un ValueError."""
    detector = DataDriftDetector()
    with pytest.raises(ValueError, match="no pueden ser nulos"):
        detector.detect_drift(None, [1.0, 2.0])

def test_empty_data_raises_error():
    """Valida que pasar conjuntos vacíos lance un ValueError."""
    detector = DataDriftDetector()
    with pytest.raises(ValueError, match="no pueden estar vacíos"):
        detector.detect_drift([], [1.0, 2.0])

def test_no_drift_detected():
    """Valida que no se detecte deriva cuando las distribuciones son estadísticamente idénticas."""
    np.random.seed(42)
    ref = np.random.normal(loc=0.0, scale=1.0, size=100)
    prod = np.random.normal(loc=0.0, scale=1.0, size=100)
    
    detector = DataDriftDetector(significance_level=0.05)
    result = detector.detect_drift(ref, prod)
    
    assert isinstance(result, dict)
    assert "drift_detected" in result
    assert result["drift_detected"] is False

def test_drift_detected():
    """Valida que se detecte deriva cuando las distribuciones cambian significativamente."""
    np.random.seed(42)
    ref = np.random.normal(loc=0.0, scale=1.0, size=100)
    # Distribución shiftada artificialmente para generar drift
    prod = np.random.normal(loc=2.0, scale=1.0, size=100)
    
    detector = DataDriftDetector(significance_level=0.05)
    result = detector.detect_drift(ref, prod)
    
    assert result["drift_detected"] is True
    assert result["p_value"] < 0.05