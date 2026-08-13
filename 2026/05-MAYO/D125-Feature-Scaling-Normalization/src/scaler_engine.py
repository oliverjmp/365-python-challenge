import pandas as pd
import numpy as np
from sklearn.preprocessing import RobustScaler, PowerTransformer
from typing import Dict, Any

class FeatureScalerEngine:
    """Motor de estandarización robusta y normalización de distribuciones sesgadas."""
    
    def __init__(self, method: str = "robust", **kwargs: Any):
        self.method = method.lower()
        if self.method == "robust":
            self.scaler = RobustScaler(**kwargs)
        elif self.method == "power":
            # standard_normal=True asegura media 0 y varianza 1 tras la transformación
            self.scaler = PowerTransformer(method="yeo-johnson", standardize=True, **kwargs)
        else:
            raise ValueError(f"Método de escalado no soportado: '{method}'. Use 'robust' o 'power'.")
        
        self.is_fitted = False

    def fit_transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """Ajusta el transformador y escala las características numéricas del DataFrame."""
        if df.empty:
            raise ValueError("El DataFrame de entrada está vacío.")
        
        columns = df.columns
        index = df.index
        
        scaled_array = self.scaler.fit_transform(df)
        self.is_fitted = True
        
        return pd.DataFrame(scaled_array, columns=columns, index=index)

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """Transforma nuevos datos usando los parámetros previamente ajustados."""
        if not self.is_fitted:
            raise ValueError("El motor de escalado debe ser ajustado (fit_transform) antes de transformar nuevos datos.")
        if df.empty:
            raise ValueError("El DataFrame de entrada está vacío.")
            
        columns = df.columns
        index = df.index
        scaled_array = self.scaler.transform(df)
        
        return pd.DataFrame(scaled_array, columns=columns, index=index)