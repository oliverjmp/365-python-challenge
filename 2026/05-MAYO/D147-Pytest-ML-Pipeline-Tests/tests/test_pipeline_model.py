import pytest
import numpy as np
import pandas as pd
from src.pipeline_model import MLPipelineModel

@pytest.fixture
def synthetic_data():
    """Fixture que provee datos sintéticos para entrenamiento y pruebas."""
    np.random.seed(42)
    X = np.random.randn(50, 3)
    y = np.random.randint(0, 2, size=50)
    return X, y

@pytest.fixture
def trained_model(synthetic_data):
    """Fixture que provee un modelo MLPipelineModel ya ajustado."""
    X, y = synthetic_data
    model = MLPipelineModel(C=1.0)
    model.fit(X, y)
    return model

def test_unfitted_model_raises_runtime_error(synthetic_data):
    """Valida que intentar predecir con un modelo no ajustado lance un RuntimeError."""
    X, _ = synthetic_data
    model = MLPipelineModel()
    
    with pytest.raises(RuntimeError, match="debe ser ajustado"):
        model.predict(X)
        
    with pytest.raises(RuntimeError, match="debe ser ajustado"):
        model.predict_proba(X)

def test_empty_training_data_raises_value_error():
    """Valida que pasar datos vacíos al entrenar lance un ValueError."""
    model = MLPipelineModel()
    with pytest.raises(ValueError, match="no pueden estar vacíos"):
        model.fit([], [])

def test_mismatched_dimensions_raises_value_error(synthetic_data):
    """Valida que discrepancias de dimensiones entre X e y lancen un ValueError."""
    X, y = synthetic_data
    model = MLPipelineModel()
    with pytest.raises(ValueError, match="debe coincidir con la longitud de y"):
        model.fit(X, y[:10])

def test_empty_prediction_data_raises_value_error(trained_model):
    """Valida que predecir con conjuntos vacíos lance un ValueError."""
    with pytest.raises(ValueError, match="no puede estar vacío"):
        trained_model.predict([])

    with pytest.raises(ValueError, match="no puede estar vacío"):
        trained_model.predict_proba([])

def test_pipeline_successful_training_and_prediction(trained_model, synthetic_data):
    """Valida el flujo exitoso de predicción y consistencia de dimensiones de salida."""
    X, _ = synthetic_data
    preds = trained_model.predict(X)
    probas = trained_model.predict_proba(X)

    assert isinstance(preds, np.ndarray)
    assert len(preds) == len(X)
    assert probas.shape == (len(X), 2)
    assert all(p in [0, 1] for p in preds)