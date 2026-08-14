import numpy as np
from xgboost import XGBClassifier
from typing import Dict, Union, List, Any

class XGBoostModel:
    """Clase envoltorio para entrenar, evaluar y extraer importancias usando XGBoost Classifier."""
    
    def __init__(self, n_estimators: int = 100, max_depth: int = 3, learning_rate: float = 0.1, random_state: int = 42, **kwargs):
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.learning_rate = learning_rate
        self.random_state = random_state
        self.kwargs = kwargs
        
        self.model = XGBClassifier(
            n_estimators=self.n_estimators,
            max_depth=self.max_depth,
            learning_rate=self.learning_rate,
            random_state=self.random_state,
            eval_metric="logloss",
            **self.kwargs
        )
        self.is_fitted = False

    def fit(self, X: Union[np.ndarray, list], y: Union[np.ndarray, list]) -> None:
        """Entrena el modelo XGBoost con los datos proporcionados."""
        X_arr = np.array(X)
        y_arr = np.array(y)
        
        if len(X_arr) == 0 or len(y_arr) == 0:
            raise ValueError("Los datos de entrenamiento no pueden estar vacíos.")
            
        self.model.fit(X_arr, y_arr)
        self.is_fitted = True

    def predict(self, X: Union[np.ndarray, list]) -> np.ndarray:
        """Realiza predicciones de clase utilizando el modelo entrenado."""
        if not self.is_fitted:
            raise RuntimeError("El modelo debe ser entrenado antes de realizar predicciones.")
            
        X_arr = np.array(X)
        if len(X_arr) == 0:
            raise ValueError("Los datos de entrada para predicción no pueden estar vacíos.")
            
        return self.model.predict(X_arr)

    def predict_proba(self, X: Union[np.ndarray, list]) -> np.ndarray:
        """Calcula las probabilidades asociadas para cada clase."""
        if not self.is_fitted:
            raise RuntimeError("El modelo debe ser entrenado antes de calcular probabilidades.")
            
        X_arr = np.array(X)
        if len(X_arr) == 0:
            raise ValueError("Los datos de entrada para probabilidades no pueden estar vacíos.")
            
        return self.model.predict_proba(X_arr)

    def get_feature_importances(self) -> List[float]:
        """Retorna las importancias de las características calculadas por XGBoost."""
        if not self.is_fitted:
            raise RuntimeError("El modelo debe ser entrenado antes de obtener las importancias de características.")
            
        return self.model.feature_importances_.tolist()