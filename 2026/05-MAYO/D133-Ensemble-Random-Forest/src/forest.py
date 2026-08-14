import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.base import BaseEstimator
from typing import Dict, Union, List, Any

class RandomForestModel:
    """Clase envoltorio para entrenar, evaluar y extraer importancias de un Random Forest Classifier."""
    
    def __init__(self, n_estimators: int = 100, max_depth: Union[int, None] = None, random_state: int = 42, **kwargs):
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.random_state = random_state
        self.kwargs = kwargs
        
        self.model = RandomForestClassifier(
            n_estimators=self.n_estimators,
            max_depth=self.max_depth,
            random_state=self.random_state,
            **self.kwargs
        )
        self.is_fitted = False

    def fit(self, X: Union[np.ndarray, list], y: Union[np.ndarray, list]) -> None:
        """Entrena el modelo Random Forest con los datos proporcionados."""
        X_arr = np.array(X)
        y_arr = np.array(y)
        
        if len(X_arr) == 0 or len(y_arr) == 0:
            raise ValueError("Los datos de entrenamiento no pueden estar vacíos.")
            
        self.model.fit(X_arr, y_arr)
        self.is_fitted = True

    def predict(self, X: Union[np.ndarray, list]) -> np.ndarray:
        """Realiza predicciones utilizando el modelo entrenado."""
        if not self.is_fitted:
            raise RuntimeError("El modelo debe ser entrenado antes de realizar predicciones.")
            
        X_arr = np.array(X)
        if len(X_arr) == 0:
            raise ValueError("Los datos de entrada para predicción no pueden estar vacíos.")
            
        return self.model.predict(X_arr)

    def get_feature_importances(self) -> List[float]:
        """Retorna las importancias de las características calculadas por el bosque."""
        if not self.is_fitted:
            raise RuntimeError("El modelo debe ser entrenado antes de obtener las importancias de características.")
            
        return self.model.feature_importances_.tolist()