import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from typing import Union, Dict, Any

class PCADimensionalityEngine:
    """Motor de reducción de dimensionalidad mediante Análisis de Componentes Principales (PCA)."""
    
    def __init__(self, n_components: Union[int, float] = 0.95, **kwargs: Any):
        self.n_components = n_components
        self.pca = PCA(n_components=self.n_components, **kwargs)
        self.is_fitted = False

    def fit_transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """Ajusta el modelo PCA y reduce la dimensionalidad del DataFrame."""
        if df.empty:
            raise ValueError("El DataFrame de entrada está vacío.")
        
        index = df.index
        reduced_array = self.pca.fit_transform(df)
        self.is_fitted = True
        
        # Generar nombres dinámicos para las nuevas componentes principales
        columns = [f"PC{i+1}" for i in range(reduced_array.shape[1])]
        
        return pd.DataFrame(reduced_array, columns=columns, index=index)

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """Transforma nuevos datos proyectándolos sobre las componentes principales ajustadas."""
        if not self.is_fitted:
            raise ValueError("El motor PCA debe ser ajustado (fit_transform) antes de transformar nuevos datos.")
        if df.empty:
            raise ValueError("El DataFrame de entrada está vacío.")
            
        index = df.index
        reduced_array = self.pca.transform(df)
        columns = [f"PC{i+1}" for i in range(reduced_array.shape[1])]
        
        return pd.DataFrame(reduced_array, columns=columns, index=index)

    @property
    def explained_variance_ratio(self) -> np.ndarray:
        """Retorna la proporción de varianza explicada por cada componente principal."""
        if not self.is_fitted:
            raise ValueError("El motor PCA no ha sido ajustado todavía.")
        return self.pca.explained_variance_ratio_