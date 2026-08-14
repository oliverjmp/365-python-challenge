import numpy as np
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.base import BaseEstimator
from typing import Dict, Any, Union

class HyperparameterTuner:
    """Motor automatizado para la optimización de hiperparámetros en modelos de Machine Learning."""

    def __init__(self, estimator: BaseEstimator, cv: int = 5, scoring: str = "accuracy", random_state: int = 42):
        self.estimator = estimator
        self.cv = cv
        self.scoring = scoring
        self.random_state = random_state

        if self.cv < 2:
            raise ValueError("El número de pliegues (cv) debe ser mayor o igual a 2.")

    def grid_search(self, param_grid: Dict[str, list], X: Union[np.ndarray, list], y: Union[np.ndarray, list]) -> Dict[str, Any]:
        """Ejecuta una búsqueda exhaustiva en cuadrícula (GridSearchCV)."""
        X_arr, y_arr = np.array(X), np.array(y)
        if len(X_arr) == 0 or len(y_arr) == 0:
            raise ValueError("Los conjuntos de datos X e y no pueden estar vacíos.")

        grid = GridSearchCV(
            estimator=self.estimator,
            param_grid=param_grid,
            cv=self.cv,
            scoring=self.scoring,
            n_jobs=-1
        )
        grid.fit(X_arr, y_arr)

        return {
            "search_type": "GridSearchCV",
            "best_params": grid.best_params_,
            "best_score": float(grid.best_score_),
            "best_estimator": grid.best_estimator_
        }

    def random_search(self, param_distributions: Dict[str, Any], X: Union[np.ndarray, list], y: Union[np.ndarray, list], n_iter: int = 10) -> Dict[str, Any]:
        """Ejecuta una búsqueda aleatorizada de hiperparámetros (RandomizedSearchCV)."""
        X_arr, y_arr = np.array(X), np.array(y)
        if len(X_arr) == 0 or len(y_arr) == 0:
            raise ValueError("Los conjuntos de datos X e y no pueden estar vacíos.")
        if n_iter < 1:
            raise ValueError("El número de iteraciones (n_iter) debe ser al menos 1.")

        random_cv = RandomizedSearchCV(
            estimator=self.estimator,
            param_distributions=param_distributions,
            n_iter=n_iter,
            cv=self.cv,
            scoring=self.scoring,
            random_state=self.random_state,
            n_jobs=-1
        )
        random_cv.fit(X_arr, y_arr)

        return {
            "search_type": "RandomizedSearchCV",
            "best_params": random_cv.best_params_,
            "best_score": float(random_cv.best_score_),
            "best_estimator": random_cv.best_estimator_
        }