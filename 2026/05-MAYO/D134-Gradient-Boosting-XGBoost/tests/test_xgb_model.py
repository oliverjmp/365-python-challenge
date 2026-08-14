import pytest
import numpy as np
from src.xgb_model import XGBoostModel

def test_unfitted_model_raises_error():
    """Valida que intentar predecir, obtener probabilidades u obtener importancias sin entrenar lance un error."""
    xgb = XGBoostModel()
    
    with pytest.raises(RuntimeError, match="debe ser entrenado"):
        xgb.predict([[1, 2, 3, 4]])
        
    with pytest.raises(RuntimeError, match="debe ser entrenado"):
        xgb.predict_proba([[1, 2, 3, 4]])
        
    with pytest.raises(RuntimeError, match="debe ser entrenado"):
        xgb.get_feature_importances()

def test_empty_training_data_raises_error():
    """Valida que datasets vacíos en el entrenamiento lancen un ValueError."""
    xgb = XGBoostModel()
    with pytest.raises(ValueError, match="no pueden estar vacíos"):
        xgb.fit([], [])

def test_empty_prediction_data_raises_error():
    """Valida que datasets vacíos en la predicción o cálculo de probabilidades lancen un ValueError."""
    np.random.seed(42)
    X = np.random.randn(20, 3)
    y = np.random.randint(0, 2, size=20)
    
    xgb = XGBoostModel()
    xgb.fit(X, y)
    
    with pytest.raises(ValueError, match="no pueden estar vacíos"):
        xgb.predict([])
        
    with pytest.raises(ValueError, match="no pueden estar vacíos"):
        xgb.predict_proba([])

def test_xgboost_training_and_prediction():
    """Valida el flujo completo de entrenamiento, predicción, probabilidades e importancias con XGBoost."""
    np.random.seed(42)
    X = np.random.randn(50, 4)
    y = np.random.randint(0, 2, size=50)
    
    xgb = XGBoostModel(n_estimators=10, max_depth=2, learning_rate=0.1, random_state=42)
    xgb.fit(X, y)
    
    preds = xgb.predict(X[:5])
    assert len(preds) == 5
    
    probas = xgb.predict_proba(X[:5])
    assert probas.shape == (5, 2)
    
    importances = xgb.get_feature_importances()
    assert len(importances) == 4
    assert sum(importances) > 0.0