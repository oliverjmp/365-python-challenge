import pytest
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from src.tuner import HyperparameterTuner

def test_invalid_cv_raises_error():
    """Valida que un valor de pliegues cv menor a 2 genere una excepción."""
    model = DecisionTreeClassifier()
    with pytest.raises(ValueError, match="debe ser mayor o igual a 2"):
        HyperparameterTuner(estimator=model, cv=1)

def test_empty_data_raises_error():
    """Valida que pasar arrays vacíos genere excepciones en Grid Search y Random Search."""
    model = DecisionTreeClassifier()
    tuner = HyperparameterTuner(estimator=model, cv=3)
    param_grid = {"max_depth": [3, 5]}

    with pytest.raises(ValueError, match="no pueden estar vacíos"):
        tuner.grid_search(param_grid, [], [])

    with pytest.raises(ValueError, match="no pueden estar vacíos"):
        tuner.random_search(param_grid, [], [], n_iter=2)

def test_invalid_n_iter_raises_error():
    """Valida que un n_iter menor a 1 genere un error en Random Search."""
    model = DecisionTreeClassifier()
    tuner = HyperparameterTuner(estimator=model, cv=3)
    param_grid = {"max_depth": [3, 5]}

    with pytest.raises(ValueError, match="debe ser al menos 1"):
        tuner.random_search(param_grid, [[1, 2], [3, 4]], [0, 1], n_iter=0)

def test_grid_search_success():
    """Valida la ejecución correcta de Grid Search."""
    np.random.seed(42)
    X = np.random.randn(40, 4)
    y = np.random.randint(0, 2, size=40)

    model = DecisionTreeClassifier(random_state=42)
    tuner = HyperparameterTuner(estimator=model, cv=3, scoring="accuracy")
    param_grid = {"max_depth": [2, 4, 6], "criterion": ["gini", "entropy"]}

    result = tuner.grid_search(param_grid, X, y)

    assert result["search_type"] == "GridSearchCV"
    assert "max_depth" in result["best_params"]
    assert 0.0 <= result["best_score"] <= 1.0

def test_random_search_success():
    """Valida la ejecución correcta de Random Search."""
    np.random.seed(42)
    X = np.random.randn(40, 4)
    y = np.random.randint(0, 2, size=40)

    model = DecisionTreeClassifier(random_state=42)
    tuner = HyperparameterTuner(estimator=model, cv=3, scoring="accuracy")
    param_dist = {"max_depth": [2, 3, 4, 5, 6], "min_samples_split": [2, 3, 4]}

    result = tuner.random_search(param_dist, X, y, n_iter=3)

    assert result["search_type"] == "RandomizedSearchCV"
    assert "max_depth" in result["best_params"]
    assert 0.0 <= result["best_score"] <= 1.0