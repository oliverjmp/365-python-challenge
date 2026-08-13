import pytest
import pandas as pd
import numpy as np
from src.pca_engine import PCADimensionalityEngine

def test_empty_dataframe_raises_error():
    """Valida que se lance un error si el DataFrame está vacío."""
    engine = PCADimensionalityEngine(n_components=2)
    df_empty = pd.DataFrame()
    with pytest.raises(ValueError, match="DataFrame de entrada está vacío"):
        engine.fit_transform(df_empty)

def test_transform_without_fit_raises_error():
    """Valida que falle si se intenta transformar sin ajustar antes."""
    engine = PCADimensionalityEngine(n_components=2)
    df = pd.DataFrame({"a": [1.0, 2.0], "b": [3.0, 4.0], "c": [5.0, 6.0]})
    with pytest.raises(ValueError, match="debe ser ajustado"):
        engine.transform(df)

def test_transform_empty_dataframe_raises_error():
    """Valida que falle si se intenta transformar un DataFrame vacío con un motor ajustado."""
    data = {"a": [1.0, 2.0, 3.0], "b": [4.0, 5.0, 6.0], "c": [7.0, 8.0, 9.0]}
    df = pd.DataFrame(data)
    engine = PCADimensionalityEngine(n_components=2)
    engine.fit_transform(df)
    
    df_empty = pd.DataFrame()
    with pytest.raises(ValueError, match="DataFrame de entrada está vacío"):
        engine.transform(df_empty)

def test_explained_variance_unfitted_raises_error():
    """Valida que consultar la varianza explicada sin ajustar lance un error."""
    engine = PCADimensionalityEngine()
    with pytest.raises(ValueError, match="no ha sido ajustado todavía"):
        _ = engine.explained_variance_ratio

def test_pca_reduction_with_int_components():
    """Valida la reducción de dimensionalidad especificando un número entero de componentes."""
    np.random.seed(42)
    data = np.random.rand(10, 5)  # 10 muestras, 5 características
    df = pd.DataFrame(data, columns=[f"feat_{i}" for i in range(5)])
    
    engine = PCADimensionalityEngine(n_components=2)
    result = engine.fit_transform(df)
    
    assert len(result) == 10
    assert result.shape[1] == 2
    assert list(result.columns) == ["PC1", "PC2"]
    
    # Probar transform en nuevos datos
    new_data = pd.DataFrame(np.random.rand(3, 5), columns=df.columns)
    transformed_new = engine.transform(new_data)
    assert transformed_new.shape == (3, 2)
    assert len(engine.explained_variance_ratio) == 2

def test_pca_reduction_with_variance_threshold():
    """Valida la reducción de dimensionalidad preservando un porcentaje de varianza (ej. 90%)."""
    np.random.seed(42)
    data = np.random.rand(20, 4)
    df = pd.DataFrame(data, columns=["a", "b", "c", "d"])
    
    engine = PCADimensionalityEngine(n_components=0.90)
    result = engine.fit_transform(df)
    
    assert len(result) == 20
    assert result.shape[1] <= 4
    assert np.sum(engine.explained_variance_ratio) >= 0.90