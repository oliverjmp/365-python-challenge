import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.base import BaseEstimator
from typing import Union, List

class MLPipelineModel:
    """Modelo de Machine Learning basado en Pipeline con preprocesamiento y clasificación."""

    def __init__(self, C: float = 1.0):
        self.C = C
        self.pipeline = Pipeline([
            ('scaler', StandardScaler()),
            ('classifier', LogisticRegression(C=self.C, random_state=42))
        ])
        self.is_fitted = False

    def fit(self, X: Union[pd.DataFrame, np.ndarray, list], y: Union[pd.Series, np.ndarray, list]) -> None:
        """Ajusta el pipeline con los datos de entrenamiento."""
        X_df = pd.DataFrame(X) if not isinstance(X, pd.DataFrame) else X
        y_arr = np.array(y)

        if X_df.empty or len(y_arr) == 0:
            raise ValueError("Los datos de entrenamiento X e y no pueden estar vacíos.")
        if len(X_df) != len(y_arr):
            raise ValueError("El número de filas en X debe coincidir con la longitud de y.")

        self.pipeline.fit(X_df, y_arr)
        self.is_fitted = True

    def predict(self, X: Union[pd.DataFrame, np.ndarray, list]) -> np.ndarray:
        """Realiza predicciones usando el pipeline ajustado."""
        if not self.is_fitted:
            raise RuntimeError("El modelo debe ser ajustado (fit) antes de realizar predicciones.")
        
        X_df = pd.DataFrame(X) if not isinstance(X, pd.DataFrame) else X
        if X_df.empty:
            raise ValueError("El conjunto de datos de entrada para predicción no puede estar vacío.")

        return self.pipeline.predict(X_df)

    def predict_proba(self, X: Union[pd.DataFrame, np.ndarray, list]) -> np.ndarray:
        """Calcula probabilidades de predicción."""
        if not self.is_fitted:
            raise RuntimeError("El modelo debe ser ajustado antes de calcular probabilidades.")
        
        X_df = pd.DataFrame(X) if not isinstance(X, pd.DataFrame) else X
        if X_df.empty:
            raise ValueError("El conjunto de datos de entrada no puede estar vacío.")

        return self.pipeline.predict_proba(X_df)