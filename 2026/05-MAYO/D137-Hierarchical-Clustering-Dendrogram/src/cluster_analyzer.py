import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
from typing import Dict, Any, Union, Tuple

class HierarchicalClusterAnalyzer:
    """Motor especializado en el análisis de conglomerados jerárquicos y generación de dendrogramas."""

    def __init__(self, data: Union[np.ndarray, list], method: str = "ward", metric: str = "euclidean"):
        self.data = np.array(data)
        self.method = method
        self.metric = metric

        if len(self.data) == 0:
            raise ValueError("El conjunto de datos no puede estar vacío.")
        if self.data.ndim != 2:
            raise ValueError("El conjunto de datos debe ser una matriz bidimensional (n_samples, n_features).")

    def compute_linkage(self) -> np.ndarray:
        """Calcula la matriz de enlace jerárquico (linkage matrix) para los datos."""
        return linkage(self.data, method=self.method, metric=self.metric)

    def extract_clusters(self, linkage_matrix: np.ndarray, threshold: float, criterion: str = "distance") -> np.ndarray:
        """Forma conglomerados planos a partir de la matriz de enlace según un criterio y umbral."""
        if threshold < 0:
            raise ValueError("El umbral (threshold) no puede ser negativo.")
        return fcluster(linkage_matrix, t=threshold, criterion=criterion)

    def get_dendrogram_data(self, linkage_matrix: np.ndarray, truncate_mode: str = None, p: int = 30) -> Dict[str, Any]:
        """Calcula y retorna la estructura de datos asociada al dendrograma sin renderizarlo directamente."""
        dendro_dict = dendrogram(
            linkage_matrix,
            truncate_mode=truncate_mode,
            p=p,
            no_plot=True
        )
        return dendro_dict