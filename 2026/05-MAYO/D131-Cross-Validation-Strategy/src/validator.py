import numpy as np
from sklearn.model_selection import KFold, StratifiedKFold, cross_val_score
from sklearn.base import BaseEstimator
from typing import Dict, Union, List

class CrossValidationStrategy:
    """Motor de validación cruzada avanzado para evaluar la robustez y generalización de modelos."""
    
    def __init__(self, n_splits: int = 5, shuffle: bool = True, random_state: int = 42):
        self.n_splits = n_splits
        self.shuffle = shuffle
        self.random_state = random_state

        if self.n_splits < 2:
            raise ValueError("El número de particiones (n_splits) debe ser al menos 2.")

    def evaluate_kfold(self, model: BaseEstimator, X: Union[np.ndarray, list], y: Union[np.ndarray, list], scoring: str = 'accuracy') -> Dict[str, Union[float, List[float]]]:
        """Evalúa un modelo utilizando K-Fold Cross-Validation estándar."""
        X_arr = np.array(X)
        y_arr = np.array(y)
        
        if len(X_arr) == 0 or len(y_arr) == 0:
            raise ValueError("Los datos de entrada no pueden estar vacíos.")

        kf = KFold(n_splits=self.n_splits, shuffle=self.shuffle, random_state=self.random_state if self.shuffle else None)
        scores = cross_val_score(model, X_arr, y_arr, cv=kf, scoring=scoring)

        return {
            "strategy": "K-Fold",
            "scores": scores.tolist(),
            "mean_score": float(np.mean(scores)),
            "std_score": float(np.std(scores))
        }

    def evaluate_stratified_kfold(self, model: BaseEstimator, X: Union[np.ndarray, list], y: Union[np.ndarray, list], scoring: str = 'accuracy') -> Dict[str, Union[float, List[float]]]:
        """Evalúa un modelo utilizando Stratified K-Fold para preservar la proporción de las clases."""
        X_arr = np.array(X)
        y_arr = np.array(y)
        
        if len(X_arr) == 0 or len(y_arr) == 0:
            raise ValueError("Los datos de entrada no pueden estar vacíos.")

        skf = StratifiedKFold(n_splits=self.n_splits, shuffle=self.shuffle, random_state=self.random_state if self.shuffle else None)
        scores = cross_val_score(model, X_arr, y_arr, cv=skf, scoring=scoring)

        return {
            "strategy": "Stratified K-Fold",
            "scores": scores.tolist(),
            "mean_score": float(np.mean(scores)),
            "std_score": float(np.std(scores))
        }