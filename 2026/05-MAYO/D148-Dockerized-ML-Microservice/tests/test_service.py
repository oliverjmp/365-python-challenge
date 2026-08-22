import pytest
import numpy as np
import pandas as pd
from src.service import MLInferenceService

def test_service_initialization_and_readiness():
    """Valida que el servicio se inicialice correctamente y esté listo."""
    service = MLInferenceService()
    assert service.is_ready is True

def test_service_prediction_success():
    """Valida una predicción exitosa con datos de lista y pandas DataFrame."""
    service = MLInferenceService()
    
    # Prueba con lista
    result_list = service.predict([[1.5, 1.5]])
    assert result_list["status"] == "success"
    assert len(result_list["predictions"]) == 1

    # Prueba con DataFrame
    df_features = pd.DataFrame([[2.0, 2.0], [3.5, 4.0]])
    result_df = service.predict(df_features)
    assert result_df["status"] == "success"
    assert len(result_df["predictions"]) == 2

def test_empty_features_raises_value_error():
    """Valida que un input vacío lance un ValueError."""
    service = MLInferenceService()
    # Actualizado el match para que coincida exactamente con "no pueden estar vacías"
    with pytest.raises(ValueError, match="no pueden estar vacías"):
        service.predict([])

def test_service_not_ready_raises_runtime_error():
    """Valida que si el servicio no está listo, lance un RuntimeError."""
    service = MLInferenceService()
    service.is_ready = False
    with pytest.raises(RuntimeError, match="no está listo"):
        service.predict([[1.0, 1.0]])