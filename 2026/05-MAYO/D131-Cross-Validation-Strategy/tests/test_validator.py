import pytest
import numpy as np
from sklearn.linear_model import LogisticRegression
from src.validator import CrossValidationStrategy

def test_invalid_n_splits_raises_error():
    """Valida que un número de particiones menor a 2 lance un error."""
    with pytest.raises(ValueError, match="debe ser al menos 2"):
        CrossValidationStrategy(n_splits=1)

def test_empty_data_raises_error():
    """Valida que datasets vacíos lancen un error en las evaluaciones."""
    validator = CrossValidationStrategy(n_splits=3)
    model = LogisticRegression()
    
    with pytest.raises(ValueError, match="no pueden estar vacíos"):
        validator.evaluate_kfold(model, [], [])
        
    with pytest.raises(ValueError, match="no pueden estar vacíos"):
        validator.evaluate_stratified_kfold(model, [], [])

def test_kfold_evaluation_success():
    """Valida el funcionamiento correcto de la estrategia K-Fold."""
    np.random.seed(42)
    X = np.random.randn(50, 4)
    y = np.random.randint(0, 2, size=50)
    
    validator = CrossValidationStrategy(n_splits=3)
    model = LogisticRegression()
    
    result = validator.evaluate_kfold(model, X, y, scoring='accuracy')
    
    assert result["strategy"] == "K-Fold"
    assert len(result["scores"]) == 3
    assert 0.0 <= result["mean_score"] <= 1.0
    assert result["std_score"] >= 0.0

def test_stratified_kfold_evaluation_success():
    """Valida el funcionamiento correcto de la estrategia Stratified K-Fold."""
    np.random.seed(42)
    X = np.random.randn(50, 4)
    y = np.array([0]*40 + [1]*10) # Desbalanceado intencionalmente
    
    validator = CrossValidationStrategy(n_splits=3)
    model = LogisticRegression()
    
    result = validator.evaluate_stratified_kfold(model, X, y, scoring='accuracy')
    
    assert result["strategy"] == "Stratified K-Fold"
    assert len(result["scores"]) == 3
    assert 0.0 <= result["mean_score"] <= 1.0
    assert result["std_score"] >= 0.0