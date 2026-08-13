import pytest
import pandas as pd
import numpy as np
from src.imputation_engine import DataImputationEngine

def test_invalid_method_raises_error():
    """Valida que se lance un error si se selecciona un método desconocido."""
    with pytest.raises(ValueError, match="Método de imputación no soportado"):
        DataImputationEngine(method="invalid_method")

def test_empty_dataframe_raises_error():
    """Valida que se lance un error si el DataFrame está vacío."""
    engine = DataImputationEngine(method="knn")
    df_empty = pd.DataFrame()
    
    # Validar fit_transform con DataFrame vacío
    with pytest.raises(ValueError, match="DataFrame de entrada está vacío"):
        engine.fit_transform(df_empty)

def test_transform_without_fit_raises_error():
    """Valida que falle si se intenta transformar sin haber ajustado el modelo antes."""
    engine = DataImputationEngine(method="knn")
    df = pd.DataFrame({"a": [1.0, 2.0], "b": [3.0, 4.0]})
    with pytest.raises(ValueError, match="debe ser ajustado"):
        engine.transform(df)

def test_transform_empty_dataframe_raises_error():
    """Valida que se lance un error si se intenta transformar un DataFrame vacío con un motor ya ajustado."""
    data = {"a": [1.0, 2.0], "b": [3.0, 4.0]}
    df = pd.DataFrame(data)
    engine = DataImputationEngine(method="knn")
    engine.fit_transform(df)
    
    df_empty = pd.DataFrame()
    with pytest.raises(ValueError, match="DataFrame de entrada está vacío"):
        engine.transform(df_empty)

def test_knn_imputation_success():
    """Valida el funcionamiento correcto del pipeline de imputación KNN."""
    data = {
        "feature_1": [1.0, 2.0, np.nan, 4.0],
        "feature_2": [10.0, np.nan, 30.0, 40.0]
    }
    df = pd.DataFrame(data)
    
    engine = DataImputationEngine(method="knn", n_neighbors=2)
    result_df = engine.fit_transform(df)
    
    assert not result_df.isnull().any().any()
    assert len(result_df) == 4
    
    # Validar transformación de nuevos datos
    new_data = pd.DataFrame({"feature_1": [np.nan], "feature_2": [20.0]})
    transformed_new = engine.transform(new_data)
    assert not transformed_new.isnull().any().any()

def test_iterative_imputation_success():
    """Valida el funcionamiento correcto del pipeline de imputación Iterativa (MICE)."""
    data = {
        "feature_1": [1.0, 2.0, np.nan, 4.0],
        "feature_2": [10.0, 20.0, 30.0, np.nan]
    }
    df = pd.DataFrame(data)
    
    engine = DataImputationEngine(method="iterative", random_state=42)
    result_df = engine.fit_transform(df)
    
    assert not result_df.isnull().any().any()
    assert len(result_df) == 4