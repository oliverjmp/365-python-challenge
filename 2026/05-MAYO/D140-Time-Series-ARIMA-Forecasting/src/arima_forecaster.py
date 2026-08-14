import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA

class ARIMAForecaster:
    def __init__(self, order=(1, 1, 1)):
        self.order = order
        self.model = None
        self.fitted_model = None
        self.is_fitted = False

    def fit(self, y):
        if y is None or len(y) == 0:
            raise ValueError("Los datos no pueden estar vacíos.")
        
        y_series = pd.Series(y)
        if y_series.isna().any():
            raise ValueError("La serie temporal contiene valores nulos.")

        try:
            self.model = ARIMA(y, order=self.order)
            self.fitted_model = self.model.fit()
            self.is_fitted = True
        except Exception as e:
            if isinstance(e, ValueError):
                raise e
            raise RuntimeError(f"Error al ajustar el modelo ARIMA: {e}")

    def forecast(self, steps=1):
        if not self.is_fitted:
            raise RuntimeError("El modelo debe ser ajustado antes de pronosticar.")
        if steps <= 0:
            raise ValueError("El número de pasos debe ser mayor a cero.")
        
        forecast_result = self.fitted_model.forecast(steps=steps)
        return np.array(forecast_result)

    def get_summary(self):
        if not self.is_fitted:
            raise RuntimeError("El modelo debe estar ajustado para obtener el resumen.")
        return str(self.fitted_model.summary())