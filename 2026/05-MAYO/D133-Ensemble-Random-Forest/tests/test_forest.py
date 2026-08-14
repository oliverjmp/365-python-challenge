import pytest
import numpy as np
from src.forest import RandomForestModel

def test_unfitted_model_raises_error():
    """Valida que intentar predecir u obtener importancias sin entrenar lance un error."""
    rf = RandomForestModel()
    
    with pytest.raises(RuntimeError, match="debe ser entrenado"):
        rf.predict([[1, 2, 3, 4]])
        
    with pytest.raises(RuntimeError, match="debe ser entrenado"):
        rf.get_feature_importances()

def test_empty_training_data_raises_error():
    """Valida que datasets vacíos en el entrenamiento lancen un ValueError."""
    rf = RandomForestModel()
    with pytest.raises(ValueError, match="no pueden estar vacíos"):
        rf.fit([], [])

def test_empty_prediction_data_raises_error():
    """Valida que datasets vacíos en la predicción lancen un ValueError."""
    np.random.seed(42)
    X = np.random.randn(20, 3)
    y = np.random.randint(0, 2, size=20)
    
    rf = RandomForestModel()
    rf.fit(X, y)
    
    with pytest.raises(ValueError, match="no pueden estar vacíos"):
        rf.predict([])

def test_random_forest_training_and_prediction():
    """Valida el flujo completo de entrenamiento, predicción e importancias."""
    np.random.seed(42)
    X = np.random.randn(50, 4)
    y = np.random.randint(0, 2, size=50)
    
    rf = RandomForestModel(n_estimators=10, max_depth=3, random_state=42)
    rf.fit(X, y)
    
    preds = rf.predict(X[:5])
    assert len(preds) == 5
    
    importances = rf.get_feature_importances()
    assert len(importances) == 4
    assert sum(importances) == pytest.approx(1.0)