import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from typing import Dict, Any, Tuple

class MultipleLinearRegressionEngine:
    """Motor de regresión lineal múltiple con análisis de residuos y evaluación de homocedasticidad."""
    
    def __init__(self, **kwargs: Any):
        self.model = LinearRegression(**kwargs)
        self.is_fitted = False
        self.feature_names_ = []

    def fit(self, X: pd.DataFrame, y: pd.Series) -> 'MultipleLinearRegressionEngine':
        """Ajusta el modelo de regresión lineal múltiple a los datos de entrenamiento."""
        if X.empty or y.empty:
            raise ValueError("Los datos de entrada (X o y) están vacíos.")
        if len(X) != len(y):
            raise ValueError("El número de muestras en X y y no coincide.")
            
        self.feature_names_ = list(X.columns)
        self.model.fit(X, y)
        self.is_fitted = True
        return self

    def predict(self, X: pd.DataFrame) -> np.ndarray:
        """Genera predicciones para un conjunto de características."""
        if not self.is_fitted:
            raise ValueError("El modelo debe ser ajustado (fit) antes de realizar predicciones.")
        if X.empty:
            raise ValueError("El DataFrame de entrada está vacío.")
            
        return self.model.predict(X)

    def evaluate(self, X: pd.DataFrame, y: pd.Series) -> Dict[str, float]:
        """Evalúa el modelo calculando MSE, RMSE y R²."""
        predictions = self.predict(X)
        mse = mean_squared_error(y, predictions)
        rmse = np.sqrt(mse)
        r2 = r2_score(y, predictions)
        
        return {
            "mse": float(mse),
            "rmse": float(rmse),
            "r2": float(r2)
        }

    def analyze_residuals(self, X: pd.DataFrame, y: pd.Series) -> pd.DataFrame:
        """Calcula los residuos (y_real - y_pred) para análisis de homocedasticidad."""
        predictions = self.predict(X)
        # Asegurar que y sea un array unidimensional de numpy
        y_true = y.values if isinstance(y, pd.Series) else np.array(y)
        residuals = y_true - predictions
        
        analysis_df = pd.DataFrame({
            "y_true": y_true,
            "y_pred": predictions,
            "residual": residuals
        })
        return analysis_df

    @property
    def coefficients(self) -> Dict[str, float]:
        """Retorna un diccionario con los coeficientes asociados a cada característica."""
        if not self.is_fitted:
            raise ValueError("El modelo no ha sido ajustado todavía.")
        return dict(zip(self.feature_names_, self.model.coef_))

    @property
    def intercept(self) -> float:
        """Retorna el término independiente (intercepto) del modelo."""
        if not self.is_fitted:
            raise ValueError("El modelo no ha sido ajustado todavía.")
        return float(self.model.intercept_)