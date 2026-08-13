import pytest
from src.anomaly_detector import MultivariateAnomalyDetector

@pytest.fixture
def detector():
    return MultivariateAnomalyDetector(contamination=0.2, random_state=42)

def test_detector_not_fitted_error(detector):
    """Valida que se lance un error si se intenta predecir sin entrenar el modelo."""
    with pytest.raises(ValueError, match="debe ser entrenado"):
        detector.predict([[1.0, 2.0]])

def test_detector_fit_and_predict(detector):
    """Valida el entrenamiento y la detección correcta de puntos normales y atípicos."""
    # Datos de entrenamiento normales (clustering central muy denso)
    normal_data = [
        [10.0, 10.0],
        [10.1, 10.1],
        [9.9, 9.9],
        [10.0, 10.1],
        [9.8, 10.0],
        [10.2, 10.0],
        [10.0, 9.8],
        [10.1, 10.2]
    ]
    
    detector.fit(normal_data)
    
    # Datos a evaluar incluyendo uno idéntico al centro y uno extremadamente atípico
    test_data = [
        [10.0, 10.0],   # Punto normal dentro del cluster de entrenamiento
        [500.0, -500.0] # Anomalía extrema evidente
    ]
    
    result = detector.predict(test_data)
    
    # SOLUCIÓN: Usamos '==' en lugar de 'is' para que evalúe correctamente los np.bool_
    assert result["predictions"][0] == 1
    assert result["anomaly_flags"][0] == False
    
    # Validamos que la anomalía extrema sea detectada
    assert result["predictions"][1] == -1
    assert result["anomaly_flags"][1] == True
    assert result["total_anomalies"] >= 1