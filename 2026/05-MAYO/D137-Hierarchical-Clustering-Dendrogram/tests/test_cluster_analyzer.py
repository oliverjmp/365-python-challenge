import pytest
import numpy as np
from src.cluster_analyzer import HierarchicalClusterAnalyzer

def test_empty_data_raises_error():
    """Valida que se lance un error si se inicializa con datos vacíos."""
    with pytest.raises(ValueError, match="no puede estar vacío"):
        HierarchicalClusterAnalyzer([])

def test_invalid_dimensions_raises_error():
    """Valida que se lance un error si los datos no son bidimensionales."""
    with pytest.raises(ValueError, match="bidimensional"):
        HierarchicalClusterAnalyzer([1, 2, 3, 4])

def test_negative_threshold_raises_error():
    """Valida que un umbral negativo al extraer conglomerados genere un error."""
    data = [[1, 2], [1, 4], [1, 0]]
    analyzer = HierarchicalClusterAnalyzer(data)
    Z = analyzer.compute_linkage()
    with pytest.raises(ValueError, match="no puede ser negativo"):
        analyzer.extract_clusters(Z, threshold=-1.0)

def test_hierarchical_clustering_success():
    """Valida el flujo completo exitoso: linkage, extracción de clusters y datos de dendrograma."""
    np.random.seed(42)
    data = np.random.rand(15, 3)

    analyzer = HierarchicalClusterAnalyzer(data, method="ward", metric="euclidean")
    
    # 1. Matriz de enlace
    Z = analyzer.compute_linkage()
    assert isinstance(Z, np.ndarray)
    assert Z.shape == (data.shape[0] - 1, 4)

    # 2. Extracción de clusters
    clusters = analyzer.extract_clusters(Z, threshold=1.5, criterion="distance")
    assert len(clusters) == data.shape[0]

    # 3. Datos del dendrograma
    dendro_data = analyzer.get_dendrogram_data(Z, truncate_mode="lastp", p=5)
    assert "icoord" in dendro_data
    assert "dcoord" in dendro_data