import pytest
import numpy as np
import pandas as pd
from src.kmeans_clusterer import KMeansClusterEngine

def test_invalid_n_clusters_raises_error():
    """Valida que un número de clústeres menor a 1 lance una excepción."""
    with pytest.raises(ValueError, match="debe ser al menos 1"):
        KMeansClusterEngine(n_clusters=0)

def test_empty_input_fit_raises_error():
    """Valida que entradas vacías (DataFrame o array) lancen error en fit_predict."""
    engine = KMeansClusterEngine(n_clusters=3)
    
    with pytest.raises(ValueError, match="DataFrame de entrada está vacío"):
        engine.fit_predict(pd.DataFrame())
        
    with pytest.raises(ValueError, match="arreglo de datos de entrada está vacío"):
        engine.fit_predict(np.array([]))

def test_predict_without_fit_raises_error():
    """Valida que intentar predecir sin entrenar lance un error."""
    engine = KMeansClusterEngine(n_clusters=2)
    with pytest.raises(ValueError, match="debe ser ajustado"):
        engine.predict([[1, 2], [3, 4]])

def test_properties_without_fit_raises_error():
    """Valida que consultar propiedades sin entrenar lance errores."""
    engine = KMeansClusterEngine(n_clusters=2)
    with pytest.raises(ValueError, match="no ha sido ajustado todavía"):
        _ = engine.cluster_centers
        
    with pytest.raises(ValueError, match="no ha sido ajustado todavía"):
        _ = engine.inertia

def test_empty_input_predict_raises_error():
    """Valida que predecir con datos vacíos tras ajustar lance una excepción."""
    engine = KMeansClusterEngine(n_clusters=2)
    X = np.random.rand(10, 2)
    engine.fit_predict(X)
    
    with pytest.raises(ValueError, match="DataFrame de entrada está vacío"):
        engine.predict(pd.DataFrame())
        
    with pytest.raises(ValueError, match="arreglo de datos de entrada está vacío"):
        engine.predict(np.array([]))

def test_kmeans_clustering_success_with_dataframe():
    """Valida el funcionamiento exitoso de K-Means usando pandas DataFrames."""
    np.random.seed(42)
    df = pd.DataFrame({
        "ingresos_anuales": np.random.rand(50) * 100,
        "score_gasto": np.random.rand(50) * 100
    })
    
    engine = KMeansClusterEngine(n_clusters=3)
    labels = engine.fit_predict(df)
    
    assert len(labels) == 50
    assert set(labels).issubset({0, 1, 2})
    assert engine.cluster_centers.shape == (3, 2)
    assert engine.inertia > 0.0
    
    # Probar predicción en nuevos datos
    new_df = pd.DataFrame({
        "ingresos_anuales": [50.0, 20.0],
        "score_gasto": [80.0, 10.0]
    })
    new_labels = engine.predict(new_df)
    assert len(new_labels) == 2