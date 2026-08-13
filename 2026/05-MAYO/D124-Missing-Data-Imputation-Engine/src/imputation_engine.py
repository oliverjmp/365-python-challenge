import pandas as pd
import numpy as np
from sklearn.experimental import enable_iterative_imputer  # ¡Obligatorio para IterativeImputer!
from sklearn.impute import KNNImputer, IterativeImputer
from typing import Dict, Any, Optional

class DataImputationEngine:
    """Motor inteligente para imputación de valores nulos usando KNN e IterativeImputer (MICE)."""
    
    def __init__(self, method: str = "knn", **kwargs: Any):
        self.method = method.lower()
        if self.method == "knn":
            n_neighbors = kwargs.get("n_neighbors", 2)
            self.imputer = KNNImputer(n_neighbors=n_neighbors)
        elif self.method == "iterative":
            random_state = kwargs.get("random_state", 42)
            self.imputer = IterativeImputer(random_state=random_state, max_iter=10)
        else:
            raise ValueError(f"Método de imputación no soportado: '{method}'. Use 'knn' o 'iterative'.")
        
        self.is_fitted = False

    def fit_transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """Ajusta el imputador y transforma el DataFrame rellenando los valores nulos."""
        if df.empty:
            raise ValueError("El DataFrame de entrada está vacío.")
        
        columns = df.columns
        index = df.index
        
        imputed_array = self.imputer.fit_transform(df)
        self.is_fitted = True
        
        return pd.DataFrame(imputed_array, columns=columns, index=index)

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """Transforma nuevos datos utilizando el modelo de imputación ya ajustado."""
        if not self.is_fitted:
            raise ValueError("El motor de imputación debe ser ajustado (fit_transform) antes de transformar nuevos datos.")
        if df.empty:
            raise ValueError("El DataFrame de entrada está vacío.")
            
        columns = df.columns
        index = df.index
        imputed_array = self.imputer.transform(df)
        
        return pd.DataFrame(imputed_array, columns=columns, index=index)