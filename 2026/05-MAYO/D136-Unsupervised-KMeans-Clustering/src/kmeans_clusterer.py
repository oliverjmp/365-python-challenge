import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from typing import Union, Dict, Any

class KMeansClusterEngine:
    """Motor de agrupamiento no supervisado mediante K-Means para segmentación de bases de datos de clientes."""

    def __init__(self, n_clusters: int = 3, random_state: int = 42, **kwargs: Any):
        if n_clusters < 1:
            raise ValueError("El número de clústeres (n_clusters) debe ser al menos 1.")
        self.n_clusters = n_clusters
        self.random_state = random_state
        self.kmeans = KMeans(n_clusters=self.n_clusters, random_state=self.random_state, n_init=10, **kwargs)
        self.is_fitted = False

    def fit_predict(self, data: Union[pd.DataFrame, np.ndarray]) -> np.ndarray:
        """Ajusta el modelo K-Means y predice las etiquetas de clúster para los datos."""
        if isinstance(data, pd.DataFrame):
            if data.empty:
                raise ValueError("El DataFrame de entrada está vacío.")
            X = data.values
        else:
            X = np.array(data)
            if X.size == 0:
                raise ValueError("El arreglo de datos de entrada está vacío.")

        labels = self.kmeans.fit_predict(X)
        self.is_fitted = True
        return labels

    def predict(self, data: Union[pd.DataFrame, np.ndarray]) -> np.ndarray:
        """Asigna nuevos puntos de datos a los clústeres previamente entrenados."""
        if not self.is_fitted:
            raise ValueError("El modelo K-Means debe ser ajustado (fit_predict) antes de predecir nuevos datos.")
        
        if isinstance(data, pd.DataFrame):
            if data.empty:
                raise ValueError("El DataFrame de entrada está vacío.")
            X = data.values
        else:
            X = np.array(data)
            if X.size == 0:
                raise ValueError("El arreglo de datos de entrada está vacío.")

        return self.kmeans.predict(X)

    @property
    def cluster_centers(self) -> np.ndarray:
        """Retorna las coordenadas de los centroides de los clústeres."""
        if not self.is_fitted:
            raise ValueError("El modelo K-Means no ha sido ajustado todavía.")
        return self.kmeans.cluster_centers_

    @property
    def inertia(self) -> float:
        """Retorna la inercia (suma de las distancias al cuadrado de las muestras a su centroide más cercano)."""
        if not self.is_fitted:
            raise ValueError("El modelo K-Means no ha sido ajustado todavía.")
        return float(self.kmeans.inertia_)