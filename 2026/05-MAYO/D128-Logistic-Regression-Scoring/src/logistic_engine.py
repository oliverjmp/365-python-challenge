import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from typing import Dict, Any, List, Union

class LogisticScoringEngine:
    """Motor de clasificación binaria para estimación de probabilidad de eventos y scoring."""
    
    def __init__(self, **kwargs: Any):
        self.model = LogisticRegression(**kwargs)
        self.is_fitted = False

    def fit(self, X: Union[pd.DataFrame, np.ndarray], y: Union[pd.Series, np.ndarray]) -> None:
        """Ajusta el modelo de Regresión Logística con los datos de entrenamiento."""
        if isinstance(X, pd.DataFrame) and X.empty:
            raise ValueError("El conjunto de características X está vacío.")
        if len(X) == 0 or len(y) == 0:
            raise ValueError("Los datos de entrenamiento no pueden estar vacíos.")
        
        self.model.fit(X, y)
        self.is_fitted = True

    def predict_proba(self, X: Union[pd.DataFrame, np.ndarray]) -> np.ndarray:
        """Estima las probabilidades de pertenencia a las clases (scoring)."""
        if not self.is_fitted:
            raise ValueError("El modelo debe ser ajustado (fit) antes de predecir probabilidades.")
        if isinstance(X, pd.DataFrame) and X.empty:
            raise ValueError("El DataFrame de entrada está vacío.")
            
        return self.model.predict_proba(X)

    def predict(self, X: Union[pd.DataFrame, np.ndarray]) -> np.ndarray:
        """Predice las clases binarias (0 o 1) para las muestras de entrada."""
        if not self.is_fitted:
            raise ValueError("El modelo debe ser ajustado (fit) antes de realizar predicciones.")
        if isinstance(X, pd.DataFrame) and X.empty:
            raise ValueError("El DataFrame de entrada está vacío.")
            
        return self.model.predict(X)

    @property
    def coefficients(self) -> np.ndarray:
        """Retorna los coeficientes aprendidos por el modelo."""
        if not self.is_fitted:
            raise ValueError("El modelo no ha sido ajustado todavía.")
        return self.model.coef_