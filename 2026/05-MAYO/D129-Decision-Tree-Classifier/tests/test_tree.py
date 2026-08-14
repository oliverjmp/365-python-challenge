import pytest
import pandas as pd
import numpy as np
from src.tree_engine import DecisionTreeEngine

def test_unfitted_model_raises_error():
    """Valida que se lancen errores si se opera con el modelo sin ajustar."""
    engine = DecisionTreeEngine()
    X = np.array([[1.0, 2.0]])
    
    with pytest.raises(ValueError, match="debe ser ajustado"):
        engine.predict(X)
        
    with pytest.raises(ValueError, match="debe ser ajustado"):
        engine.predict_proba(X)
        
    with pytest.raises(ValueError, match="no ha sido ajustado"):
        _ = engine.feature_importances
        
    with pytest.raises(ValueError, match="debe ser ajustado"):
        engine.export_tree_dot()

def test_empty_training_data_raises_error():
    """Valida que falle si se entrena con datos vacíos."""
    engine = DecisionTreeEngine()
    
    with pytest.raises(ValueError, match="está vacío"):
        engine.fit(pd.DataFrame(), pd.Series([0, 1]))
        
    with pytest.raises(ValueError, match="está vacío"):
        engine.fit([], [])
        
    with pytest.raises(ValueError, match="no pueden estar vacíos"):
        engine.fit(np.array([[1.0, 2.0]]), np.array([]))

def test_empty_prediction_data_raises_error():
    """Valida que falle si se intenta predecir con estructuras vacías."""
    engine = DecisionTreeEngine()
    X_train = pd.DataFrame({"a": [1.0, 2.0], "b": [3.0, 4.0]})
    y_train = [0, 1]
    engine.fit(X_train, y_train)
    
    with pytest.raises(ValueError, match="está vacío"):
        engine.predict(pd.DataFrame())
        
    with pytest.raises(ValueError, match="está vacío"):
        engine.predict_proba(pd.DataFrame())
        
    with pytest.raises(ValueError, match="está vacío"):
        engine.predict(np.array([]))
        
    with pytest.raises(ValueError, match="está vacío"):
        engine.predict_proba(np.array([]))

def test_decision_tree_success_flow():
    """Valida el flujo completo de entrenamiento, predicción, importancias y exportación DOT."""
    np.random.seed(42)
    X_train = np.array([
        [0.1, 0.2],
        [0.2, 0.1],
        [8.0, 9.0],
        [8.5, 8.8]
    ])
    y_train = np.array([0, 0, 1, 1])
    
    engine = DecisionTreeEngine(criterion="entropy", max_depth=3, random_state=42)
    engine.fit(X_train, y_train)
    
    assert engine.is_fitted is True
    assert len(engine.feature_importances) == 2
    
    X_test = np.array([
        [0.15, 0.15],
        [8.2, 8.9]
    ])
    preds = engine.predict(X_test)
    probs = engine.predict_proba(X_test)
    
    assert len(preds) == 2
    assert preds[0] == 0
    assert preds[1] == 1
    assert probs.shape == (2, 2)
    
    dot_data = engine.export_tree_dot()
    assert "digraph Tree" in dot_data
    assert "feature_0" in dot_data