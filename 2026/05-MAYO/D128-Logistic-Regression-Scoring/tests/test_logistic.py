import pytest
import pandas as pd
import numpy as np
from src.logistic_engine import LogisticScoringEngine

def test_unfitted_model_raises_error():
    """Valida que se lance un error si se intenta predecir sin entrenar el modelo."""
    engine = LogisticScoringEngine()
    X = np.array([[1.0, 2.0]])
    
    with pytest.raises(ValueError, match="debe ser ajustado"):
        engine.predict(X)
        
    with pytest.raises(ValueError, match="debe ser ajustado"):
        engine.predict_proba(X)
        
    with pytest.raises(ValueError, match="no ha sido ajustado"):
        _ = engine.coefficients

def test_empty_training_data_raises_error():
    """Valida que falle si se intenta entrenar con datos vacíos o DataFrame vacío."""
    engine = LogisticScoringEngine()
    
    # Cubre el caso de DataFrame vacío (línea 16)
    with pytest.raises(ValueError, match="está vacío"):
        engine.fit(pd.DataFrame(), pd.Series([0, 1]))
        
    # Cubre el caso general de listas vacías
    with pytest.raises(ValueError, match="no pueden estar vacíos"):
        engine.fit([], [])

def test_empty_dataframe_prediction_raises_error():
    """Valida que falle si se pasa un DataFrame vacío para predecir o predecir probabilidades."""
    engine = LogisticScoringEngine()
    X_train = pd.DataFrame({"a": [1.0, 2.0], "b": [3.0, 4.0]})
    y_train = [0, 1]
    engine.fit(X_train, y_train)
    
    with pytest.raises(ValueError, match="está vacío"):
        engine.predict(pd.DataFrame())
        
    # Cubre la validación de predict_proba con DataFrame vacío (línea 28)
    with pytest.raises(ValueError, match="está vacío"):
        engine.predict_proba(pd.DataFrame())

def test_logistic_scoring_success():
    """Valida el flujo completo de entrenamiento, estimación de probabilidad y clasificación."""
    np.random.seed(42)
    X_train = np.array([
        [1.0, 0.5],
        [1.5, 1.2],
        [8.0, 8.5],
        [9.1, 8.2]
    ])
    y_train = np.array([0, 0, 1, 1])
    
    engine = LogisticScoringEngine(random_state=42)
    engine.fit(X_train, y_train)
    
    assert engine.is_fitted is True
    assert engine.coefficients.shape == (1, 2)
    
    X_test = np.array([[1.1, 0.9], [8.5, 8.0]])
    probs = engine.predict_proba(X_test)
    preds = engine.predict(X_test)
    
    assert probs.shape == (2, 2)
    assert len(preds) == 2
    assert preds[0] == 0
    assert preds[1] == 1